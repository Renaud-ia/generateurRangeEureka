class RangePoker:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self):
        self.combos: dict[str, float] = {}

    def to_dict(self) -> dict[str, float]:
        return self.combos

    @classmethod
    def from_dict(cls, json_range: dict[str: float]):
        instance = cls()

        # on remplit les combos non trouvés
        for combo in RangePoker.tous_les_combos_tries():
            if combo not in json_range.keys():
                json_range[combo] = 0

        instance.combos = json_range
        return instance

    def generer_input(self) -> list[float]:
        input_as_float: list[float] = []

        for combo in self.tous_les_combos_tries():
            input_as_float.append(self.combos[combo])

        return input_as_float

    @classmethod
    def tous_les_combos_tries(cls):
        combos_tries: list[str] = []

        for rank1 in cls.ranks:
            inf_ranks: list[str] = [r for r in cls.ranks if
                                    cls.ranks.index(r) <= cls.ranks.index(rank1)]
            for rank2 in inf_ranks:
                if rank1 == rank2:
                    combos_tries.append(rank1 + rank2)

                else:
                    combos_tries.append(rank1 + rank2 + "o")
                    combos_tries.append(rank1 + rank2 + "s")

        return combos_tries
