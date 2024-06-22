import os
from abc import ABC, abstractmethod

from poker import RangePoker


class BaseModelMl(ABC):
    DIR_SAVE = "saved_models"
    REPORT_DIR = os.path.join(DIR_SAVE, "reports")
    def __init__(self):
        self.data: list[list[float]] = []

        self._creer_repertoires()

    def add_data(self, ranges: list[RangePoker]):
        for range_poker in ranges:
            self.data.append(range_poker.generer_input())

    @abstractmethod
    def train(self):
        raise NotImplementedError()

    @abstractmethod
    def save_model(self):
        raise NotImplementedError()

    def _creer_repertoires(self):
        os.makedirs(self.DIR_SAVE, exist_ok=True)
        os.makedirs(self.REPORT_DIR, exist_ok=True)
