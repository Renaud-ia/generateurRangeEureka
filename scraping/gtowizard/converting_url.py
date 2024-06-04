from abc import ABC, abstractmethod


class ConvertInParameters(ABC):
    @abstractmethod
    def generate_parameters(self) -> dict[str, str]:
        raise NotImplementedError()

