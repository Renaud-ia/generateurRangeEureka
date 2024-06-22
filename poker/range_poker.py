class RangePoker:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

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
        input_as_float: list[float] = []

        for rank1 in RangePoker.ranks:
            inf_ranks: list[str] = [r for r in RangePoker.ranks if RangePoker.ranks.index(r) <= RangePoker.ranks.index(rank1)]
            for rank2 in inf_ranks:
                if rank1 == rank2:
                    input_as_float.append(self.combos[rank1 + rank2])

                else:
                    input_as_float.append(self.combos[rank1 + rank2 + "o"])
                    input_as_float.append(self.combos[rank1 + rank2 + "s"])

        return input_as_float
