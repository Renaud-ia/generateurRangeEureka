import json

from persistence import Enregistreur
from poker import VariantePoker, SituationPoker, RangePoker


class JsonEnregistreur(Enregistreur):
    def __init__(self, variante_poker: str):
        self.nom_repertoire: str = "json"
        super().__init__(variante_poker, self.nom_repertoire)

    def _charger_fichier(self, adresse_fichier: str):
        with open(self.adresse_fichier, 'r', encoding='utf-8') as fichier:
            return json.load(fichier)

    def _fixer_statut(self, statut: bool):
        self.donnees["statut"] = statut

    def ajouter_range(self, situation: SituationPoker, poker_range: RangePoker) -> bool:
        if self.donnees[situation.encode()]:
            return False

        self.donnees[situation.encode()] = poker_range.to_dict()
        return True

    def enregistrement_termine(self) -> bool:
        return self.donnees["statut"]

    def sauvegarder(self):
        with open(self.adresse_fichier, 'w', encoding='utf-8') as fichier:
            json.dump(self.donnees, fichier, indent=4)

    @classmethod
    def obt_nom_repertoire(cls):
        return self.nom_repertoire
