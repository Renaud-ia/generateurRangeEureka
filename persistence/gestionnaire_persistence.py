import os

from poker import FormatPoker

from .enregistreur import Enregistreur
from .json_enregistreur import JsonEnregistreur


class GestionnairePersistence:
    connecteur_persistence = JsonEnregistreur

    @classmethod
    def recuperer_enregistreur(cls, format_poker: FormatPoker) -> Enregistreur:
        return cls.connecteur_persistence(format_poker.encode())

    @classmethod
    def recuperer_tous_les_enregistreurs(cls) -> list[Enregistreur]:
        enregistreurs: list[Enregistreur] = []

        repertoire: str = cls.connecteur_persistence.nom_repertoire

        for nom_fichier in os.listdir(repertoire):
            chemin_complet: str = os.path.join(repertoire, nom_fichier)
            if os.path.isfile(chemin_complet):
                enregistreurs.append(cls.connecteur_persistence(nom_fichier))

        return enregistreurs
