import json
import os.path

from .enregistreur import Enregistreur, EntreeExisteDeja
from .recuperateur import Recuperateur
from poker import SituationPoker, RangePoker, FormatPoker


class JsonEnregistreur(Enregistreur, Recuperateur):
    nom_repertoire: str = "json"

    def __init__(self, format_poker: FormatPoker):
        super().__init__(format_poker, self.nom_repertoire)

    def _charger_fichier(self, adresse_fichier: str) -> dict:
        if not os.path.exists(adresse_fichier):
            return {}

        with open(self.adresse_fichier, 'r', encoding='utf-8') as fichier:
            return json.load(fichier)

    def _fixer_statut(self, statut: bool) -> None:
        self.donnees["termine"] = statut

    def ajouter_range(self, situation: SituationPoker, poker_range: RangePoker) -> None:
        stack, situation, action = situation.to_keys()

        if action is None:
            raise ValueError("La situation est vide")

        if stack not in self.donnees.keys():
            self.donnees[stack] = {}

        if situation not in self.donnees[stack].keys():
            self.donnees[stack][situation] = {}

        if action in self.donnees[stack][situation].keys():
            raise EntreeExisteDeja(f"Entrée déjà existante [{stack}][{situation}][{action}]")

        self.donnees[stack][situation][action] = poker_range.to_dict()

    def situation_deja_enregistree(self, situation: SituationPoker) -> bool:
        stack, situation_code = situation.to_keys_next_situation()

        if stack not in self.donnees.keys():
            return False

        if situation_code not in self.donnees[stack].keys():
            return False

        return bool(self.donnees[stack][situation_code])

    def recuperer_situations_suivantes(self, situation) -> list[SituationPoker]:
        stack, situation = situation.to_keys_next_situation()

        data_situation = self.donnees[stack][situation]

        situations_suivantes: list[SituationPoker] = []

        for action in data_situation.keys():
            nouvelle_situation: SituationPoker = SituationPoker.from_keys(stack, situation, action)
            situations_suivantes.append(nouvelle_situation)

        return situations_suivantes

    def deja_scrape(self) -> bool:
        return self.donnees["termine"]

    def sauvegarder(self) -> None:
        with open(self.adresse_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(self.donnees, fichier, indent=4)

    def get_ranges_enregistrees(self) -> dict[SituationPoker, RangePoker]:
        ranges_enregistrees: dict[SituationPoker, RangePoker] = {}

        for stack in self.donnees:
            if not isinstance(self.donnees[stack], dict):
                continue
            for situation in self.donnees[stack].keys():
                if not isinstance(self.donnees[stack][situation], dict):
                    continue
                for action in self.donnees[stack][situation].keys():
                    range_dict: dict = self.donnees[stack][situation][action]

                    situation_poker: SituationPoker = SituationPoker.from_keys(stack, situation, action)
                    range_poker: RangePoker = RangePoker.from_dict(range_dict)

                    ranges_enregistrees[situation_poker] = range_poker

        return ranges_enregistrees

    def get_format_poker(self) -> FormatPoker:
        return self.format_poker
