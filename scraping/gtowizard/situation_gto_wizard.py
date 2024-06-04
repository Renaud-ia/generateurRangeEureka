from poker import SituationPoker, InitialSymmetricStacks
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
        args = {
            "stacks": "",
            "preflop_actions": "",
            "flop_actions": "",
            "turn_actions": "",
            "river_actions": "",
            "board": ""
        }

        if isinstance(self.initial_stacks, InitialSymmetricStacks):
            args["depth"] = self.initial_stacks.get_common_stack()

        else:
            raise NotImplementedError()

        return args


class SituationMttPokerGtoWizard(SituationPokerGtoWizard):
    def generate_parameters(self) -> dict[str, str]:
        args = super().generate_parameters()
        args["depth"] += 0.125

        return args

