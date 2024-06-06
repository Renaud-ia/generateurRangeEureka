import random
import unittest

from poker import InitialSymmetricStacks, RangePoker
from scraping.gtowizard.scraping_task_gto_wizard import ExtractingData
from scraping.gtowizard.situation_gto_wizard import SituationMttPokerGtoWizard, SituationPokerGtoWizard


class TestExtractingData(unittest.TestCase):
    def setUp(self):
        initial_stacks = InitialSymmetricStacks(100)
        self.situation = SituationMttPokerGtoWizard(initial_stacks)

        self.strategies: list[list] = [
            [random.uniform(0, 1) for _ in range(169)],
            [random.uniform(0, 1) for _ in range(169)],
            [random.uniform(0, 1) for _ in range(169)],
            [random.uniform(0, 1) for _ in range(169)]
        ]

    def test_chaque_action_genere_bons_parametres(self):
        expected_params = [
            "F",
            "C2.3",
            "R2.3",
            "RAI"
        ]

        response: dict = {
            "solutions": [
                {
                    "action": {
                        "code": "F",
                        "type": "FOLD",
                        "betsize": "0.000",
                        "all-in": False,
                    },
                    "strategy": self.strategies[0]
                },
                {
                    "action": {
                        "code": "C",
                        "type": "CALL",
                        "betsize": "2.3",
                        "all-in": False,
                    },
                    "strategy": self.strategies[1]
                },
                {
                    "action": {
                        "code": "R",
                        "type": "RAISE",
                        "betsize": "2.3",
                        "all-in": False,
                    },
                    "strategy": self.strategies[2]
                },
                {
                    "action": {
                        "code": "RAI",
                        "type": "RAISE",
                        "betsize": "80",
                        "all-in": True,

                    },
                    "strategy": self.strategies[2]
                }]
        }

        extracted_ranges: dict[SituationPokerGtoWizard, RangePoker] = \
            ExtractingData.extract_ranges(self.situation, response)

        self.assertTrue(len(extracted_ranges) == 4)

        for i, [new_situation, _] in enumerate(extracted_ranges.items()):
            self.assertEqual(
                expected_params[i],
                new_situation.generate_parameters()["preflop_actions"]
            )

    def test_deux_actions_genere_bons_parametres(self):
        expected_param = "F-F"

        response: dict = {
            "solutions": [
                {
                    "action": {
                        "code": "F",
                        "type": "FOLD",
                        "betsize": "0.000",
                        "all-in": False,
                    },
                    "strategy": self.strategies[0]
                }]
        }

        extracted_ranges_first_action: dict[SituationPokerGtoWizard, RangePoker] = \
            ExtractingData.extract_ranges(self.situation, response)

        first_situation = list(extracted_ranges_first_action.keys())[0]

        extracted_ranges_second_action: dict[SituationPokerGtoWizard, RangePoker] = \
            ExtractingData.extract_ranges(first_situation, response)

        second_situation = list(extracted_ranges_second_action.keys())[0]

        self.assertNotEqual(first_situation, second_situation)

        self.assertTrue(len(extracted_ranges_second_action) == 1)

        self.assertEqual(
            expected_param,
            second_situation.generate_parameters()["preflop_actions"]
        )

