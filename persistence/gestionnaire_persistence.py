import os

from poker import FormatPoker, Variante, TypeJeuPoker

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
    def recuperer_enregistreurs_externe(cls) -> list[Recuperateur]:
        noms_repertoires: list[str] = ["Cash6m50z50bbGeneral", "Cash6m50z100bbGeneral"]
        # TODO comment trouver le nom du format depuis le nom sans import réciproque ??
        format_poker: FormatPoker = FormatPoker(Variante.TEXAS_HOLDEM_NO_LIMIT, TypeJeuPoker.CASH_GAME, 6)

        recuperateurs: list[Recuperateur] = []

        for rep in noms_repertoires:
            recuperateur: RecuperateurDir = RecuperateurDir(rep, format_poker)
            recuperateurs.append(recuperateur)

        return recuperateurs






