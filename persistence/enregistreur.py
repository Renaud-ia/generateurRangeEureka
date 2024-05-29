from abc import ABC, abstractmethod
import os

from poker import RangePoker, SituationPoker, VariantePoker


class Enregistreur(ABC):
    def __init__(self, variante_poker: str, nom_repertoire: str):
        os.makedirs(nom_repertoire, exist_ok=True)
        self.repertoire: str = nom_repertoire
        self.adresse_fichier = os.path.join(nom_repertoire, variante_poker)
        self.donnees = self._charger_fichier(self.adresse_fichier)
        self._fixer_statut(False)

    def terminer_enregistrement(self):
        self._fixer_statut(True)
        self.sauvegarder()

    @abstractmethod
    def _fixer_statut(self, statut: bool):
        raise NotImplementedError()

    @abstractmethod
    def _charger_fichier(self, adresse_fichier: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def ajouter_range(self, situation: SituationPoker, poker_range: RangePoker):
        raise NotImplementedError()

    @abstractmethod
    def sauvegarder(self):
        raise NotImplementedError()

    @abstractmethod
    def enregistrement_termine(self) -> bool:
        raise NotImplementedError()
