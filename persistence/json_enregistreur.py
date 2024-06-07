import json
import os.path

from .enregistreur import Enregistreur
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

    def situation_deja_enregistree(self, situation: SituationPoker) -> bool:
        return False

    def ajouter_range(self, situation: SituationPoker, poker_range: RangePoker) -> bool:
        if situation.to_key() in self.donnees:
            return False

        self.donnees[situation.to_key()] = poker_range.to_dict()
        return True

    def deja_scrape(self) -> bool:
        return self.donnees["termine"]

    def sauvegarder(self) -> None:
        with open(self.adresse_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(self.donnees, fichier, indent=4)

    def recuperer_situations_suivantes(self, situation_copie) -> list[SituationPoker]:
        return []
