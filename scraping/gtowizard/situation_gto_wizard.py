from poker import SituationPoker
from poker import ActionPoker, Move
from poker import InitialStacks
from .converting_url import ConvertInParameters


class ActionGtoWizard(ActionPoker):
    def __init__(self, move: Move):
        super().__init__(move)


class SituationPokerGtoWizard(SituationPoker, ConvertInParameters):
    def __init__(self,
                 initial_stacks: InitialStacks,
                 actions: list[ActionGtoWizard] = None):
        super().__init__(initial_stacks, actions)

    def generate_parameters(self) -> dict[str, str]:
        # todo
        return {}


class SituationMttPokerGtoWizard(SituationPokerGtoWizard):
    pass

