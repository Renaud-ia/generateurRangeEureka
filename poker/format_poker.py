from enum import Enum


class Variante(Enum):
    TEXAS_HOLDEM_NO_LIMIT = "TexasHoldemNoLimit"


class TypeJeuPoker(Enum):
    MTT = "MTT"
    MTT_KO = "MTTKO"
    MTT_ICM = "MTTICM"
    CASH_GAME = "CashGame"
    SPIN = "SPIN&GO"


class FormatPoker:
    def __init__(self,
                 variante: Variante,
                 type_jeu: TypeJeuPoker,
                 n_joueurs: int
                 ):
        self.variante = variante
        self.type_jeu = type_jeu
        self.n_joueurs = n_joueurs

    # génère une string pour persistence
    def to_key(self) -> str:
        return f"{self.variante.value}_{self.type_jeu.value}_{self.n_joueurs}"

    @classmethod
    def from_key(cls, nom_fichier: str):
        encoded_info: list[str] = nom_fichier.split("_")

        if len(encoded_info) != 3:
            raise ValueError(f"Le nom n'a pas été bien encodé: {nom_fichier}")

        variante: Variante = Variante(encoded_info[0])
        type_jeu: TypeJeuPoker = TypeJeuPoker(encoded_info[1])
        n_joueurs: int = int(encoded_info[2])

        return cls(variante, type_jeu, n_joueurs)
