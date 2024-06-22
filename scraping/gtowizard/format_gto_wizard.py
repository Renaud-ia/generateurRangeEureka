from abc import abstractmethod, ABC

from poker import FormatPoker, InitialSymmetricStacks
from poker import Variante, TypeJeuPoker
from poker import InitialStacks
from scraping.gtowizard.converting_url import ConvertInParameters


class FormatGtoWizard(FormatPoker, ConvertInParameters):
    def __init__(self,
                 variante: Variante,
                 type_jeu: TypeJeuPoker,
                 n_joueurs: int):
        super().__init__(variante, type_jeu, n_joueurs)

    @abstractmethod
    def possibles_stack_sizes(self) -> list[InitialStacks]:
        raise NotImplementedError

    @abstractmethod
    def generate_parameters(self) -> dict[str, str]:
        raise NotImplementedError


class MttStandardGtoWizard(FormatGtoWizard):
    def __init__(self):
        super().__init__(
            Variante.TEXAS_HOLDEM_NO_LIMIT,
            TypeJeuPoker.MTT,
            8
        )

    def possibles_stack_sizes(self) -> list[InitialStacks]:
        possibles_stacks: list[InitialStacks] = [
            InitialSymmetricStacks(2),
            InitialSymmetricStacks(3),
            InitialSymmetricStacks(4),
            InitialSymmetricStacks(5),
            InitialSymmetricStacks(6),
            InitialSymmetricStacks(7),
            InitialSymmetricStacks(8),
            InitialSymmetricStacks(9),
            InitialSymmetricStacks(10),
            InitialSymmetricStacks(12),
            InitialSymmetricStacks(14),
            InitialSymmetricStacks(17),
            InitialSymmetricStacks(20),
            InitialSymmetricStacks(25),
            InitialSymmetricStacks(30),
            InitialSymmetricStacks(35),
            InitialSymmetricStacks(40),
            InitialSymmetricStacks(50),
            InitialSymmetricStacks(60),
            InitialSymmetricStacks(80),
            InitialSymmetricStacks(100)
        ]

        return possibles_stacks

    def generate_parameters(self) -> dict[str, str]:
        return {"gametype": "MTTGeneral"}


class CashGameClassicGtoWizard(FormatGtoWizard):
    def __init__(self):
        super().__init__(
            Variante.TEXAS_HOLDEM_NO_LIMIT,
            TypeJeuPoker.CASH_GAME,
            6
        )

    def possibles_stack_sizes(self) -> list[InitialStacks]:
        possible_stacks: list[InitialStacks] = [
            InitialSymmetricStacks(20),
            InitialSymmetricStacks(40),
            InitialSymmetricStacks(50),
            InitialSymmetricStacks(75),
            InitialSymmetricStacks(100),
            InitialSymmetricStacks(150),
            InitialSymmetricStacks(200)
        ]

        return possible_stacks

    def generate_parameters(self) -> dict[str, str]:
        return {"gametype": "Cash6m500z"}


class SpinClassicGtoWizard(FormatGtoWizard):
    def __init__(self):
        super().__init__(
            Variante.TEXAS_HOLDEM_NO_LIMIT,
            TypeJeuPoker.SPIN,
            3
        )

    def possibles_stack_sizes(self) -> list[InitialStacks]:
        possible_stacks: list[InitialStacks] = [
            InitialSymmetricStacks(1),
            InitialSymmetricStacks(1.5),
            InitialSymmetricStacks(2),
            InitialSymmetricStacks(2.5),
            InitialSymmetricStacks(3),
            InitialSymmetricStacks(3.5),
            InitialSymmetricStacks(4),
            InitialSymmetricStacks(4.5),
            InitialSymmetricStacks(5),
            InitialSymmetricStacks(5.5),
            InitialSymmetricStacks(6),
            InitialSymmetricStacks(6.5),
            InitialSymmetricStacks(7),
            InitialSymmetricStacks(7.5),
            InitialSymmetricStacks(8),
            InitialSymmetricStacks(8.5),
            InitialSymmetricStacks(9),
            InitialSymmetricStacks(9.5),
            InitialSymmetricStacks(10),
            InitialSymmetricStacks(10.5),
            InitialSymmetricStacks(11),
            InitialSymmetricStacks(11.5),
            InitialSymmetricStacks(12),
            InitialSymmetricStacks(12.5),
            InitialSymmetricStacks(13),
            InitialSymmetricStacks(13.5),
            InitialSymmetricStacks(14),
            InitialSymmetricStacks(14.5),
            InitialSymmetricStacks(15),
            InitialSymmetricStacks(16),
            InitialSymmetricStacks(17),
            InitialSymmetricStacks(18),
            InitialSymmetricStacks(19),
            InitialSymmetricStacks(20),
            InitialSymmetricStacks(21),
            InitialSymmetricStacks(22),
            InitialSymmetricStacks(23),
            InitialSymmetricStacks(24),
            InitialSymmetricStacks(25),
            InitialSymmetricStacks(30),
            InitialSymmetricStacks(35),
            InitialSymmetricStacks(40),
            InitialSymmetricStacks(45),
            InitialSymmetricStacks(50),
            InitialSymmetricStacks(55),
            InitialSymmetricStacks(60),
            InitialSymmetricStacks(72)
        ]

        return possible_stacks

    def generate_parameters(self) -> dict[str, str]:
        return {"gametype": "HuSngSimple_V3"}


class BuilderFormatGtoWizard:
    @staticmethod
    def generate_all_formats() -> list[FormatGtoWizard]:
        list_format: list[FormatGtoWizard] = []

        mtt_standard_8_joueurs = MttStandardGtoWizard()

        list_format.append(mtt_standard_8_joueurs)

        return list_format
