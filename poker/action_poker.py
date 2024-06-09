from enum import Enum


class Move(Enum):
    # ATTENTION CHAQUE ACTION DOIT COMMENCER PAR UNE LETTRE DIFFERENTE
    FOLD = "F"
    RAISE = "R"
    CALL = "C"
    RAISE_ALL_IN = "AI"


class ActionPoker:
    def __init__(self, move: Move, betsize: float = 0):
        self.move = move
        self.betsize = betsize

    def to_key(self):
        return self.move.value + (str(self.betsize) if self.betsize > 0 else "")

    @classmethod
    def from_key(cls, key):
        # Identifier la partie du move (toujours présente)
        move_part = None
        betsize_part = 0

        # Essayer de faire correspondre avec chaque move
        for move in Move:
            if key.startswith(move.value):
                move_part = move
                betsize_str = key[len(move.value):]
                if betsize_str:
                    betsize_part = float(betsize_str)
                break

        if move_part is None:
            raise ValueError(f"Invalid key format: {key}")

        return cls(move_part, betsize_part)

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, ActionPoker):
            return False

        return self.move == other.move and self.betsize == other.betsize

    def __str__(self):
        return self.move.value + (str(self.betsize) if self.betsize > 0 else "")

    def __repr__(self):
        return self.move.value + (str(self.betsize) if self.betsize > 0 else "")
