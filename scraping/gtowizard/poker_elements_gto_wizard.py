from poker import ActionPoker, Move, RangePoker


class ActionPokerGtoWizard(ActionPoker):
    converting_moves: dict[str, Move] = {
        "F": Move.FOLD,
        "C": Move.CALL,
        "R": Move.RAISE,
        "RAI": Move.RAISE_ALL_IN
    }

    def __init__(self, move_code_gto_wizard: str, betsize: float = 0):
        super().__init__(ActionPokerGtoWizard.converting_moves[move_code_gto_wizard], betsize)
        self.move_code_gto_wizard = move_code_gto_wizard

    def to_code_gto_wizard(self):
        return self.move_code_gto_wizard + (str(self.betsize) if self.move == Move.RAISE else "")


class RangeGtoWizard(RangePoker):
    # important, l'ordre d'encodage et l'ordre de génération pour chaque rank est différent
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    sorted_ranks = sorted(ranks)

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

        for sorted_rank in RangeGtoWizard.sorted_ranks:
            initial_index = RangeGtoWizard.ranks.index(sorted_rank)
            for j in range(initial_index + 1):
                if initial_index == j:
                    all_combos.append(sorted_rank + RangeGtoWizard.ranks[j])
                else:
                    all_combos.append(sorted_rank + RangeGtoWizard.ranks[j] + "o")
                    all_combos.append(sorted_rank + RangeGtoWizard.ranks[j] + "s")

        return all_combos

