import re

from poker import ActionPoker, Move, RangePoker


class ActionPokerGtoWizard(ActionPoker):
    converting_moves: dict[str, Move] = {
        "F": Move.FOLD,
        "C": Move.CALL,
        "R": Move.RAISE,
        "RAI": Move.RAISE_ALL_IN
    }

    moves_to_code: dict[Move, str] = {value: key for key, value in converting_moves.items()}

    def __init__(self, move_code_gto_wizard: str, betsize: float = 0):
        super().__init__(ActionPokerGtoWizard.converting_moves[re.sub("[^a-zA-Z]", "", move_code_gto_wizard)], betsize)
        self.move_code_gto_wizard = re.sub("[^a-zA-Z]", "", move_code_gto_wizard)

    def to_code_gto_wizard(self):
        return self.move_code_gto_wizard + (str(self.betsize) if self.move == Move.RAISE else "")

    @classmethod
    def from_poker_action(cls, action: ActionPoker):
        return cls(cls.moves_to_code[action.move], action.betsize)


class RangeGtoWizard(RangePoker):
    # important, l'ordre d'encodage et l'ordre de génération pour chaque rank est différent
    sorted_ranks = sorted(RangePoker.ranks)

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
            index_rank = RangeGtoWizard.ranks.index(sorted_rank)
            inf_ranks: list[str] = [c for c in RangeGtoWizard.sorted_ranks if RangeGtoWizard.ranks.index(c) <= index_rank]
            for inf_rank in inf_ranks:
                if inf_rank == sorted_rank:
                    all_combos.append(sorted_rank + inf_rank)
                else:
                    all_combos.append(sorted_rank + inf_rank + "o")
                    all_combos.append(sorted_rank + inf_rank + "s")

        return all_combos

