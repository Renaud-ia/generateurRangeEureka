import copy
from abc import ABC, abstractmethod
from typing import Optional

from poker.action_poker import ActionPoker, Move


class InitialStacks(ABC):
    @abstractmethod
    def to_key(self):
        raise NotImplementedError()


class InitialSymmetricStacks(InitialStacks):
    def __init__(self, amount_stack: float):
        # important: on convertit en float pour garantir l'équivalence de comparaisons
        self.initial_stack = float(amount_stack)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, InitialSymmetricStacks):
            return False
        return self.initial_stack == other.initial_stack

    def get_common_stack(self):
        return self.initial_stack

    def to_key(self):
        return f"{self.initial_stack}BB"

    @classmethod
    def from_key(cls, key: str):
        if key.endswith("BB"):
            try:
                amount_stack = float(key[:-2])
                return cls(amount_stack)
            except ValueError:
                raise ValueError(f"Invalid key format: {key}")
        else:
            raise ValueError(f"Invalid key format: {key}")

    def __str__(self):
        return f"{self.initial_stack}BB"


class InitialNonSymmetricStacks(InitialStacks):
    def to_key(self):
        raise NotImplementedError()


class SituationPoker:
    def __init__(self, initial_stacks: InitialStacks, actions: list[ActionPoker] = None):
        if actions is None:
            actions = []
        self.actions = actions
        self.initial_stacks = initial_stacks

    def ajouter_action(self, action_poker: ActionPoker):
        self.actions.append(action_poker)

    def to_keys(self) -> (str, str, str):
        return self.to_stack_key(), self.to_situation_key(), self.to_action_key()

    def to_keys_next_situation(self) -> (str, str, str):
        if len(self.actions) == 0:
            return self.to_stack_key(), "root"

        return self.to_stack_key(), self._generate_key(self.actions)

    def to_stack_key(self) -> str:
        return self.initial_stacks.to_key()

    def to_situation_key(self) -> str:
        if len(self.actions) <= 1:
            return "root"

        return self._generate_key(self.actions[:-1])

    def to_action_key(self) -> Optional[str]:
        if len(self.actions) == 0:
            return None

        return str(self.actions[-1])

    @staticmethod
    def _generate_key(actions: list[ActionPoker]):
        gen_key: str = ""
        for index, action in enumerate(actions):
            gen_key += action.to_key()
            if index < len(actions) - 1:
                gen_key += "-"

        return gen_key

    @classmethod
    def from_keys(cls, stack: str, situation: str, action: str):
        stack: InitialSymmetricStacks = InitialSymmetricStacks.from_key(stack)
        return_object: SituationPoker = cls(stack)

        for previous_action in situation.split("-"):
            if previous_action == "root":
                break
            convert_action: ActionPoker = ActionPoker.from_key(previous_action)
            return_object.ajouter_action(convert_action)

        final_action: ActionPoker = ActionPoker.from_key(action)
        return_object.ajouter_action(final_action)

        return return_object

    def __hash__(self) -> int:
        return hash('_'.join(self.to_keys()))

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, SituationPoker):
            return False

        if self.initial_stacks != other.initial_stacks:
            return False

        if len(self.actions) != len(other.actions):
            return False

        for index, action_self in enumerate(self.actions):
            if action_self != other.actions[index]:
                return False

        return True

    def __str__(self):
        return f"SITUATION {self.initial_stacks}, {self.actions}"

    def __repr__(self):
        return f"SITUATION {self.initial_stacks}, {self.actions}"
