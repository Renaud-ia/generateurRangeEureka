import copy
from typing import Any, Optional

import requests

from persistence import Enregistreur
from poker import RangePoker, SituationPoker
from .format_gto_wizard import FormatGtoWizard
from .poker_elements_gto_wizard import ActionPokerGtoWizard, RangeGtoWizard
from .situation_gto_wizard import SituationPokerGtoWizard
from ..scraping_exceptions import BearerNotValid, ErreurRequete, LimitConnexionReached


class ExtractingData:
    @staticmethod
    def extract_ranges(situation: SituationPokerGtoWizard, response: dict) -> dict[SituationPokerGtoWizard, RangePoker]:
        extracted_ranges: dict[SituationPokerGtoWizard, RangePoker] = {}

        solutions: list = response["solutions"]

        for action in solutions:
            action_convertie: ActionPokerGtoWizard = ExtractingData._convert_actions(action)

            range_as_float: list[float] = action["strategy"]
            range_convertie: RangeGtoWizard = RangeGtoWizard(range_as_float)

            nouvelle_situation = copy.deepcopy(situation)
            nouvelle_situation.ajouter_action(action_convertie)

            extracted_ranges[nouvelle_situation] = range_convertie

        return extracted_ranges

    @staticmethod
    def _convert_actions(action: dict) -> ActionPokerGtoWizard:
        code_action: str = action["action"]["code"]
        betsize: float = float(action["action"]["betsize"])

        action_convertie: ActionPokerGtoWizard = ActionPokerGtoWizard(code_action, betsize)

        return action_convertie


class ScrapingTaskGtoWizard:
    scraping_url: str = "https://gtowizard.com/api/v1/poker/solution/"

    def __init__(self, format_poker: FormatGtoWizard, situation_poker: SituationPokerGtoWizard):
        self.format_poker = format_poker
        self.situation = situation_poker

    def execute(self, bearer: str, enregistreur: Enregistreur) -> list['ScrapingTaskGtoWizard']:
        if enregistreur.situation_deja_enregistree(self.situation):
            return self.extract_tasks_from_persistence(enregistreur)

        response: dict = self._request_endpoint(bearer)

        if not response:
            return []

        ranges_scrapees: dict[SituationPokerGtoWizard, RangePoker] = \
            ExtractingData.extract_ranges(self.situation, response)
        self._save_ranges(ranges_scrapees, enregistreur)

        next_tasks: list[ScrapingTaskGtoWizard] = []

        for situation, _ in ranges_scrapees.items():
            new_task: ScrapingTaskGtoWizard = ScrapingTaskGtoWizard(self.format_poker, situation)
            next_tasks.append(new_task)

        return next_tasks

    def extract_tasks_from_persistence(self, enregistreur) -> list['ScrapingTaskGtoWizard']:
        situations_suivantes: list[SituationPoker] = enregistreur.recuperer_situations_suivantes(self.situation)

        taches_suivantes: list['ScrapingTaskGtoWizard'] = []

        for situation in situations_suivantes:
            new_situation: SituationPokerGtoWizard = SituationPokerGtoWizard.from_situation_poker(situation)
            new_task: ScrapingTaskGtoWizard = ScrapingTaskGtoWizard(self.format_poker, new_situation)
            taches_suivantes.append(new_task)

        return taches_suivantes

    def _request_endpoint(self, bearer: str) -> dict:
        headers = {
            "Authorization": f"Bearer {bearer}"
        }

        params = self.situation.generate_parameters() | self.format_poker.generate_parameters()

        response = requests.get(
            ScrapingTaskGtoWizard.scraping_url,
            params=params,
            headers=headers,
        )

        if response.status_code == 401:
            raise BearerNotValid(f"Réponse du serveur: {response}")

        elif response.status_code == 429:
            raise LimitConnexionReached(f"Compte bloqué car trop de connexions: {response}")

        # si pas de board, on a un status_code 204 au flop
        elif response.status_code == 204:
            return {}

        elif response.status_code != 200:
            raise ErreurRequete(f"Réponse du serveur: {response}, requête avec params: {params}")

        return response.json()

    def _save_ranges(self, ranges: dict[SituationPokerGtoWizard, RangePoker], enregistreur: Enregistreur):
        for situation, range_poker in ranges.items():
            enregistreur.ajouter_range(situation, range_poker)

    def __str__(self):
        return f"{self.situation}"
