from enum import Enum


class Move(Enum):
    FOLD = "F"
    RAISE = "R"
    CALL = "C"
    RAISE_ALL_IN = "RAI"


class ActionPoker:
    def __init__(self, move: Move, betsize: float = 0):
        self.move = move
        self.betsize = betsize

    def __str__(self):
        return self.move.value + str(self.betsize)

    def __repr__(self):
        return self.move.value + str(self.betsize)
