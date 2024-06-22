import unittest

from poker import InitialStacks, InitialSymmetricStacks
from scraping.gtowizard.format_gto_wizard \
    import MttStandardGtoWizard, FormatGtoWizard, CashGameClassicGtoWizard, SpinClassicGtoWizard


class TestFormatGtoWizard(unittest.TestCase):
    def test_mtt_standard_genere_bons_parametres(self):
        mtt_standard: FormatGtoWizard = MttStandardGtoWizard()

        generated_args: dict[str, str] = mtt_standard.generate_parameters()

        expected_args = {
            "gametype": "MTTGeneral"
        }

        self.assertDictEqual(generated_args, expected_args,
                             "Les arguments générés ne correspondent pas à ceux attendus")

    def test_mtt_standard_genere_bon_stacks_sizes(self):
        mtt_standard: FormatGtoWizard = MttStandardGtoWizard()

        stack_sizes: list[InitialStacks] = mtt_standard.possibles_stack_sizes()

        stacks_attendus: list[InitialStacks] = [
            InitialSymmetricStacks(100),
            InitialSymmetricStacks(80),
            InitialSymmetricStacks(60),
            InitialSymmetricStacks(50),
            InitialSymmetricStacks(40),
            InitialSymmetricStacks(35),
            InitialSymmetricStacks(30),
            InitialSymmetricStacks(25),
            InitialSymmetricStacks(20),
            InitialSymmetricStacks(17),
            InitialSymmetricStacks(14),
            InitialSymmetricStacks(12),
            InitialSymmetricStacks(10),
            InitialSymmetricStacks(9),
            InitialSymmetricStacks(8),
            InitialSymmetricStacks(7),
            InitialSymmetricStacks(6),
            InitialSymmetricStacks(5),
            InitialSymmetricStacks(4),
            InitialSymmetricStacks(3),
            InitialSymmetricStacks(2)
        ]

        self.assertCountEqual(stack_sizes, stacks_attendus, "La liste des stacks générés n'est pas bonne")

    def test_cash_game_classic_genere_bons_parametres(self):
        cash_game_classique: FormatGtoWizard = CashGameClassicGtoWizard()

        generated_args: dict[str, str] = cash_game_classique.generate_parameters()

        expected_args = {
            "gametype": "Cash6m500z"
        }

        self.assertCountEqual(generated_args, expected_args,
                             "Les arguments générés ne correspondent pas à ceux attendus")

    def test_cash_game_classic_genere_bon_stacks_sizes(self):
        cash_game_classic: FormatGtoWizard = CashGameClassicGtoWizard()

        stack_sizes: list[InitialStacks] = cash_game_classic.possibles_stack_sizes()

        stacks_attendus: list[InitialStacks] = [
            InitialSymmetricStacks(200),
            InitialSymmetricStacks(150),
            InitialSymmetricStacks(100),
            InitialSymmetricStacks(75),
            InitialSymmetricStacks(50),
            InitialSymmetricStacks(40),
            InitialSymmetricStacks(20)
        ]

        self.assertCountEqual(stack_sizes, stacks_attendus, "La liste des stacks générés n'est pas bonne")

    def test_spin_classic_genere_bons_parametres(self):
        spin_classique: FormatGtoWizard = SpinClassicGtoWizard()

        generated_args: dict[str, str] = spin_classique.generate_parameters()

        expected_args = {
            "gametype": "HuSngSimple_V3"
        }

        self.assertCountEqual(generated_args, expected_args,
                             "Les arguments générés ne correspondent pas à ceux attendus")

    def test_spin_classic_genere_bon_stacks_sizes(self):
        spin_classic: FormatGtoWizard = SpinClassicGtoWizard()

        stack_sizes: list[InitialStacks] = spin_classic.possibles_stack_sizes()

        stacks_attendus: list[InitialStacks] = [
            InitialSymmetricStacks(72),
            InitialSymmetricStacks(60),
            InitialSymmetricStacks(55),
            InitialSymmetricStacks(50),
            InitialSymmetricStacks(45),
            InitialSymmetricStacks(40),
            InitialSymmetricStacks(35),
            InitialSymmetricStacks(30),
            InitialSymmetricStacks(25),
            InitialSymmetricStacks(24),
            InitialSymmetricStacks(23),
            InitialSymmetricStacks(22),
            InitialSymmetricStacks(21),
            InitialSymmetricStacks(20),
            InitialSymmetricStacks(19),
            InitialSymmetricStacks(18),
            InitialSymmetricStacks(17),
            InitialSymmetricStacks(16),
            InitialSymmetricStacks(15),
            InitialSymmetricStacks(14.5),
            InitialSymmetricStacks(14),
            InitialSymmetricStacks(13.5),
            InitialSymmetricStacks(13),
            InitialSymmetricStacks(12.5),
            InitialSymmetricStacks(12),
            InitialSymmetricStacks(11.5),
            InitialSymmetricStacks(11),
            InitialSymmetricStacks(10.5),
            InitialSymmetricStacks(10),
            InitialSymmetricStacks(9.5),
            InitialSymmetricStacks(9),
            InitialSymmetricStacks(8.5),
            InitialSymmetricStacks(8),
            InitialSymmetricStacks(7.5),
            InitialSymmetricStacks(7),
            InitialSymmetricStacks(6.5),
            InitialSymmetricStacks(6),
            InitialSymmetricStacks(5.5),
            InitialSymmetricStacks(5),
            InitialSymmetricStacks(4.5),
            InitialSymmetricStacks(4),
            InitialSymmetricStacks(3.5),
            InitialSymmetricStacks(3),
            InitialSymmetricStacks(2.5),
            InitialSymmetricStacks(2),
            InitialSymmetricStacks(1.5),
            InitialSymmetricStacks(1)
        ]

        self.assertCountEqual(stack_sizes, stacks_attendus, "La liste des stacks générés n'est pas bonne")
