from poker import ActionPoker, Move, RangePoker


class ActionPokerGtoWizard(ActionPoker):
    converting_moves: dict[str, Move] = {
        "F": Move.FOLD,
        "R": Move.RAISE,
        "RAI": Move.RAISE_ALL_IN
    }

    def __init__(self, move: str, betsize: float):
        super().__init__(ActionPokerGtoWizard.converting_moves[move], betsize)


class RangeGtoWizard(RangePoker):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    def __init__(self, range_non_formatee: list[float]):
        super().__init__()
        all_combos_sorted: list[str] = self._generate_all_combos_sorted()

        if len(all_combos_sorted) != len(range_non_formatee):
            raise ValueError("La longueur scrapée ne correspond pas")

        for i in range(len(range_non_formatee)):
            self.combos[all_combos_sorted[i]] = range_non_formatee[i]

    @staticmethod
    def _generate_all_combos_sorted() -> list[str]:
        all_combos: list[str] = []

        for i in range(len(RangeGtoWizard.ranks)):
            for j in range(i + 1):
                if i == j:
                    all_combos.append(RangeGtoWizard.ranks[i] + RangeGtoWizard.ranks[j])

                else:
                    all_combos.append(RangeGtoWizard.ranks[i] + RangeGtoWizard.ranks[j] + "o")
                    all_combos.append(RangeGtoWizard.ranks[i] + RangeGtoWizard.ranks[j] + "s")

        return all_combos

