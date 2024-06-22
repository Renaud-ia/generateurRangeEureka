from abc import ABC, abstractmethod

from poker import SituationPoker, RangePoker, FormatPoker


class Recuperateur(ABC):
    @abstractmethod
    def get_ranges_enregistrees(self) -> dict[SituationPoker, RangePoker]:
        raise NotImplementedError()

    @abstractmethod
    def get_format_poker(self) -> FormatPoker:
        raise NotImplementedError()
