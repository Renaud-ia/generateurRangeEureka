import unittest
from typing import Union

from poker import InitialSymmetricStacks, ActionPoker, Move
from scraping.gtowizard.situation_gto_wizard import SituationPokerGtoWizard, SituationMttPokerGtoWizard


class TestFormatGtoWizardMttStandard100BBSymetric(unittest.TestCase):
    def setUp(self):
        initial_stacks = InitialSymmetricStacks(100)
        self.situation = SituationMttPokerGtoWizard(initial_stacks)

    def test_base_genere_bons_arguments(self):
        generated_args: dict[str, Union[float, str]] = self.situation.generate_parameters()

        expected_args = {
            "depth": 100.125,
            "stacks": "",
            "preflop_actions": "",
            "flop_actions": "",
            "turn_actions": "",
            "river_actions": "",
            "board": ""
        }

        self.assertDictEqual(generated_args, expected_args,
                             "Les arguments générés ne correspondent pas à ceux attendus")

    def ajout_actions_genere_bons_arguments(self):
        action1: ActionPoker = ActionPoker(Move.RAISE, 2.3)
        action2: ActionPoker = ActionPoker(Move.FOLD)
        action3: ActionPoker = ActionPoker(Move.RAISE_ALL_IN)

        self.situation.ajouter_action(action1)
        self.situation.ajouter_action(action2)
        self.situation.ajouter_action(action3)

        generated_args: dict[str, Union[float, str]] = self.situation.generate_parameters()

        self.assertIn('preflop_actions', generated_args)
        self.assertEqual(generated_args['preflop_actions'], "R2.3-F-RAI")


class TestCashGameClassic250BBSymetric(unittest.TestCase):
    def setUp(self):
        initial_stacks = InitialSymmetricStacks(200)
        self.situation = SituationPokerGtoWizard(initial_stacks)

    def test_base_genere_bons_arguments(self):
        generated_args: dict[str, Union[float, str]] = self.situation.generate_parameters()

        expected_args = {
            "depth": 200,
            "stacks": "",
            "preflop_actions": "",
            "flop_actions": "",
            "turn_actions": "",
            "river_actions": "",
            "board": ""
        }

        self.assertDictEqual(generated_args, expected_args,
                             "Les arguments générés ne correspondent pas à ceux attendus")

    def ajout_actions_genere_bons_arguments(self):
        action1: ActionPoker = ActionPoker(Move.RAISE, 2.3)
        action2: ActionPoker = ActionPoker(Move.FOLD)
        action3: ActionPoker = ActionPoker(Move.RAISE_ALL_IN)

        self.situation.ajouter_action(action1)
        self.situation.ajouter_action(action2)
        self.situation.ajouter_action(action3)

        generated_args: dict[str, Union[float, str]] = self.situation.generate_parameters()

        self.assertIn('preflop_actions', generated_args)
        self.assertEqual(generated_args['preflop_actions'], "R2.3-F-RAI")


class TestSpinClassicFloatBBSymetric(unittest.TestCase):
    def setUp(self):
        initial_stacks = InitialSymmetricStacks(13.5)
        self.situation = SituationPokerGtoWizard(initial_stacks)

    def test_base_genere_bons_arguments(self):
        generated_args: dict[str, Union[float, str]] = self.situation.generate_parameters()

        expected_args = {
            "depth": 13.5,
            "stacks": "",
            "preflop_actions": "",
            "flop_actions": "",
            "turn_actions": "",
            "river_actions": "",
            "board": ""
        }

        self.assertDictEqual(generated_args, expected_args,
                             "Les arguments générés ne correspondent pas à ceux attendus")

    def ajout_actions_genere_bons_arguments(self):
        action1: ActionPoker = ActionPoker(Move.RAISE, 2.3)
        action2: ActionPoker = ActionPoker(Move.FOLD)
        action3: ActionPoker = ActionPoker(Move.RAISE_ALL_IN)

        self.situation.ajouter_action(action1)
        self.situation.ajouter_action(action2)
        self.situation.ajouter_action(action3)

        generated_args: dict[str, Union[float, str]] = self.situation.generate_parameters()

        self.assertIn('preflop_actions', generated_args)
        self.assertEqual(generated_args['preflop_actions'], "R2.3-F-RAI")

