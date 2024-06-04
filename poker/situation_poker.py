from abc import ABC, abstractmethod

from poker.action_poker import ActionPoker


class InitialStacks(ABC):
    @abstractmethod
    def n_initial_players(self):
        raise NotImplementedError()


class InitialSymmetricStacks(InitialStacks):
    def __init__(self, amount_stack: int):
        pass
    def n_initial_players(self):
        pass


class InitialNonSymmetricStacks(InitialStacks):
    def n_initial_players(self):
        pass


class SituationPoker:
    def __init__(self, initial_stacks: InitialStacks, actions: list[ActionPoker] = None):
        if actions is None:
            actions = []
        self.actions = actions
        self.initial_stacks = initial_stacks

    def encode(self):
        pass
