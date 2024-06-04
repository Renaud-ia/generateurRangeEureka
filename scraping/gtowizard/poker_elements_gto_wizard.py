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
    def __init__(self, range_non_formatee: list[float]):
        super().__init__()
        #todo convertir la range
