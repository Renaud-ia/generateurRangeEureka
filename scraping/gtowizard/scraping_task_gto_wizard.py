import requests

from poker import RangePoker
from .format_gto_wizard import FormatGtoWizard
from .situation_gto_wizard import SituationPokerGtoWizard
from ..scraping_exceptions import BearerNotValid, ErreurRequete
from ..scraping_task import ScrapingTask


class ScrapingTaskGtoWizard(ScrapingTask):
    scraping_url: str = "https://gtowizard.com/api/v1/poker/solution/"

    def __init__(self, format_poker: FormatGtoWizard, situation_poker: SituationPokerGtoWizard):
        super().__init__(format_poker)
        self.format_poker = format_poker
        self.situation = situation_poker

    def execute(self, bearer: str) -> list['ScrapingTaskGtoWizard']:
        ranges_scrapees: dict[SituationPokerGtoWizard, RangePoker] = self._request_endpoint(bearer)
        self._save_ranges(ranges_scrapees)

        next_tasks: list[ScrapingTaskGtoWizard] = []

        for situation, _ in ranges_scrapees.items():
            new_task: ScrapingTaskGtoWizard = ScrapingTaskGtoWizard(self.format_poker, situation)
            next_tasks.append(new_task)

        return next_tasks

    def _request_endpoint(self, bearer: str) -> dict[SituationPokerGtoWizard, RangePoker]:
        headers = {
            "Authorization": f"Bearer {bearer}"
        }

        params = self.situation.generate_parameters()

        response = requests.post(
            ScrapingTaskGtoWizard.scraping_url,
            params=params,
            headers=headers)

        if response.status_code == 401:
            raise BearerNotValid(f"Réponse du serveur: {response}")

        elif response.status_code != 200:
            raise ErreurRequete(f"Réponse du serveur: {response}")

        return self._extract_ranges(response)

    def _save_ranges(self, ranges: dict[SituationPokerGtoWizard, RangePoker]):
        for situation, range_poker in ranges.items():
            self.enregistreur.ajouter_range(situation, range_poker)

        self.enregistreur.terminer_enregistrement()

    def _extract_ranges(self, response) -> dict[SituationPokerGtoWizard, RangePoker]:
        pass
