import unittest

from poker import InitialSymmetricStacks
from scraping.gtowizard.situation_gto_wizard import SituationPokerGtoWizard


class TestFormatGtoWizardMttStandard100BBSymetric(unittest.TestCase):
    def setUp(self):
        initial_stacks = InitialSymmetricStacks(100)
        self.situation = SituationPokerGtoWizard(initial_stacks)
    def test_base_genere_bons_arguments(self):
        generated_args: dict[str, str] = self.situation.generate_parameters()

        expected_args = {

        }

        self.assertDictEqual(generated_args, expected_args, "Les arguments générés ne correspondent pas à ceux attendus")



