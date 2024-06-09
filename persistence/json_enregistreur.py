import json
import os.path

from .enregistreur import Enregistreur, EntreeExisteDeja
from poker import SituationPoker, RangePoker


class JsonEnregistreur(Enregistreur):
    nom_repertoire: str = "json"

    def __init__(self, format_poker: str):
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
