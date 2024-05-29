import os

from poker import VariantePoker

from .enregistreur import Enregistreur
from .json_enregistreur import JsonEnregistreur

connecteur_persistence = JsonEnregistreur


class GestionnairePersistence:
    @classmethod
    def recuperer_enregistreur(cls, variante_poker: VariantePoker) -> Enregistreur:
        return connecteur_persistence(variante_poker.encode())

    @classmethod
    def recuperer_tous_les_enregistreurs(cls) -> list[Enregistreur]:
        enregistreurs: list[Enregistreur] = []

        repertoire: str = connecteur_persistence.nom_repertoire

        for nom_fichier in os.listdir(repertoire):
            chemin_complet: str = os.path.join(repertoire, nom_fichier)
            if os.path.isfile(chemin_complet):
                enregistreurs.append(connecteur_persistence(nom_fichier))

        return enregistreurs
