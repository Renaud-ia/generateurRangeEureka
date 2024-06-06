from poker import SituationPoker, InitialSymmetricStacks
from poker import ActionPoker, Move
from poker import InitialStacks
from . import FormatGtoWizard
from .converting_url import ConvertInParameters
from .format_gto_wizard import MttStandardGtoWizard
from .poker_elements_gto_wizard import ActionPokerGtoWizard


class SituationPokerGtoWizard(SituationPoker, ConvertInParameters):
    def __init__(self,
                 initial_stacks: InitialStacks,
                 actions: list[ActionPokerGtoWizard] = None
                 ):
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

        for index, action in enumerate(self.actions):
            if isinstance(action, ActionPokerGtoWizard):
                args["preflop_actions"] += action.to_code_gto_wizard()
            else:
                raise TypeError("Invalid action type. All actions must be instances of ActionGtoWizard.")

            if index < len(self.actions) - 1:
                args["preflop_actions"] += "-"

        if isinstance(self.initial_stacks, InitialSymmetricStacks):
            args["depth"] = self.initial_stacks.get_common_stack()

        else:
            raise NotImplementedError()

        return args

    def __str__(self):
        return super(SituationPoker, self).__str__()


class SituationMttPokerGtoWizard(SituationPokerGtoWizard):
    # pour une raison obscure, les paramètres de requête ajoutent 0.125 au stack
    def generate_parameters(self) -> dict[str, str]:
        args = super().generate_parameters()
        args["depth"] += 0.125

        return args

    def __str__(self):
        return super(SituationPokerGtoWizard, self).__str__()


class BuilderSituationGtoWizard:
    @staticmethod
    def get(format_gto_wizard: FormatGtoWizard, initial_stacks: InitialStacks):
        if isinstance(format_gto_wizard, MttStandardGtoWizard):
            return SituationMttPokerGtoWizard(initial_stacks)

        else:
            return SituationPokerGtoWizard(initial_stacks)
