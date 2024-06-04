from abc import abstractmethod, ABC

from poker import FormatPoker
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
        # todo
        pass

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
        pass

    def generate_parameters(self) -> dict[str, str]:
        pass


class SpinClassicGtoWizard(FormatGtoWizard):
    def __init__(self):
        super().__init__(
            Variante.TEXAS_HOLDEM_NO_LIMIT,
            TypeJeuPoker.SPIN,
            3
        )

    def possibles_stack_sizes(self) -> list[InitialStacks]:
        pass

    def generate_parameters(self) -> dict[str, str]:
        pass


class BuilderFormatGtoWizard:
    @staticmethod
    def generate_all_formats() -> list[FormatGtoWizard]:
        list_format: list[FormatGtoWizard] = []

        mtt_standard_8_joueurs = MttStandardGtoWizard()

        list_format.append(mtt_standard_8_joueurs)

        return list_format
