from abc import ABC, abstractmethod
import os

from poker import RangePoker, SituationPoker, FormatPoker


class EntreeExisteDeja(Exception):
    def __init__(self, message: str = ""):
        super().__init__(message)


class Enregistreur(ABC):
    def __init__(self, format_poker: str, nom_repertoire: str):
        os.makedirs(nom_repertoire, exist_ok=True)
        self.repertoire: str = nom_repertoire
        self.adresse_fichier = os.path.join(nom_repertoire, format_poker)
        self.donnees = self._charger_fichier(self.adresse_fichier)
        self._fixer_statut(False)

    def terminer_enregistrement(self) -> None:
        self._fixer_statut(True)
        self.sauvegarder()

    @abstractmethod
    def _fixer_statut(self, statut: bool) -> None:
        raise NotImplementedError()

    @abstractmethod
    def _charger_fichier(self, adresse_fichier: str) -> dict:
        raise NotImplementedError()

    @abstractmethod
    def ajouter_range(self, situation: SituationPoker, poker_range: RangePoker) -> None:
        raise NotImplementedError()

    @abstractmethod
    def situation_deja_enregistree(self, situation: SituationPoker) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def sauvegarder(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def deja_scrape(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def recuperer_situations_suivantes(self, situation_copie) -> list[SituationPoker]:
        raise NotImplementedError()
