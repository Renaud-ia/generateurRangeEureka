import unittest

from poker import InitialStacks, InitialSymmetricStacks, SituationPoker, ActionPoker, Move


class TestSituationPoker(unittest.TestCase):
    def setUp(self) -> None:
        self.stack_depart: float = 25
        stacks: InitialStacks = InitialSymmetricStacks(self.stack_depart)
        self.situation = SituationPoker(stacks)

    def test_aucune_action_creation(self):
        self.assertTrue(len(self.situation.actions) == 0)

    def test_ajout_fold(self):
        action: ActionPoker = ActionPoker(Move.FOLD)
        self.situation.ajouter_action(action)
        self.assertTrue(len(self.situation.actions) == 1)

    def test_ajout_raise(self):
        action: ActionPoker = ActionPoker(Move.RAISE, 10)
        self.situation.ajouter_action(action)
        self.assertTrue(len(self.situation.actions) == 1)

    def test_ajout_raise_all_in(self):
        action: ActionPoker = ActionPoker(Move.RAISE_ALL_IN)
        self.situation.ajouter_action(action)
        self.assertTrue(len(self.situation.actions) == 1)



