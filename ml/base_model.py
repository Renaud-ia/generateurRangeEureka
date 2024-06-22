from abc import ABC, abstractmethod

from poker import RangePoker


class BaseModelMl(ABC):
    def __init__(self):
        self.data: list[list[float]] = []

    def add_data(self, ranges: list[RangePoker]):
        for range_poker in ranges:
            self.data.append(range_poker.generer_input())

    @abstractmethod
    def train(self):
        raise NotImplementedError()

    @abstractmethod
    def save_model(self):
        raise NotImplementedError()

    @abstractmethod
    def load_model(self):
        raise NotImplementedError()

    @abstractmethod
    def predict(self, input_data: list[float]):
        raise NotImplementedError()
