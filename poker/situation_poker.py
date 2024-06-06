import copy
from abc import ABC, abstractmethod

from poker.action_poker import ActionPoker, Move


class InitialStacks(ABC):
    pass


class InitialSymmetricStacks(InitialStacks):
    def __init__(self, amount_stack: float):
        self.initial_stack = amount_stack

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, InitialSymmetricStacks):
            return False
        return self.initial_stack == other.initial_stack

    def get_common_stack(self):
        return self.initial_stack

    def __str__(self):
        return f"{self.initial_stack}BB"


class InitialNonSymmetricStacks(InitialStacks):
    pass


class SituationPoker:
    def __init__(self, initial_stacks: InitialStacks, actions: list[ActionPoker] = None):
        if actions is None:
            actions = []
        self.actions = actions
        self.initial_stacks = initial_stacks

    def ajouter_action(self, action_poker: ActionPoker):
        self.actions.append(action_poker)

    def to_key(self):
        gen_key: str = self.initial_stacks.__str__() + "_"
        for index, action in enumerate(self.actions):
            gen_key += f"{action}"
            if index < len(self.actions) - 1:
                gen_key += "-"

        return gen_key

    def __str__(self):
        return f"SITUATION {self.initial_stacks}, {self.actions}"

