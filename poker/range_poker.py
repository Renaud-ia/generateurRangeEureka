class RangePoker:
    def __init__(self):
        self.combos: dict[str, float] = {}

    def to_dict(self) -> dict[str, float]:
        return self.combos

    @classmethod
    def from_dict(cls, json_range: dict[str: float]):
        instance = cls()
        instance.combos = json_range
        return instance

    def generer_input(self) -> list[float]:
        #todo pour ML
        pass