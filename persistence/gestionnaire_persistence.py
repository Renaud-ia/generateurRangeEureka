import os

from poker import FormatPoker

from .enregistreur import Enregistreur
from .json_enregistreur import JsonEnregistreur
from .recuperateur import Recuperateur
from .recuperateur_dir import RecuperateurDir


class GestionnairePersistence:
    connecteur_persistence = JsonEnregistreur

    @classmethod
    def recuperer_enregistreur(cls, format_poker: FormatPoker) -> Enregistreur:
        return cls.connecteur_persistence(format_poker)

    @classmethod
    def recuperer_enregistreurs_json(cls) -> list[Recuperateur]:
        enregistreurs: list[Recuperateur] = []

        repertoire: str = cls.connecteur_persistence.nom_repertoire

        for nom_fichier in os.listdir(repertoire):
            chemin_complet: str = os.path.join(repertoire, nom_fichier)
            if os.path.isfile(chemin_complet):
                format_poker: FormatPoker = FormatPoker.from_key(nom_fichier)
                enregistreurs.append(cls.connecteur_persistence(format_poker))

        return enregistreurs

    @classmethod
    def recuperer_enregistreurs_externe(cls):
        return [RecuperateurDir("Cash6m50z50bbGeneral"), RecuperateurDir("Cash6m50z100bbGeneral")]






