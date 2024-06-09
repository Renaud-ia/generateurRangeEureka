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

    def test_deux_fold_is_leaf(self):
        n_joueurs = 3
        fold_action = ActionPoker(Move.FOLD)

        self.situation.ajouter_action(fold_action)
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(fold_action)

        self.assertTrue(self.situation.is_leaf(n_joueurs))

    def test_call_call_call_is_leaf(self):
        n_joueurs = 3

        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))

        self.assertTrue(self.situation.is_leaf(n_joueurs))

    def test_raise_call_call_is_leaf(self):
        n_joueurs = 3

        self.situation.ajouter_action(ActionPoker(Move.RAISE))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))

        self.assertTrue(self.situation.is_leaf(n_joueurs))

    def test_raise_call_raise_not_leaf(self):
        n_joueurs = 3

        self.situation.ajouter_action(ActionPoker(Move.RAISE))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.RAISE))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertTrue(self.situation.is_leaf(n_joueurs))

    def test_fold_all_in_call(self):
        n_joueurs = 8

        self.situation.ajouter_action(ActionPoker(Move.FOLD))
        self.situation.ajouter_action(ActionPoker(Move.FOLD))
        self.situation.ajouter_action(ActionPoker(Move.FOLD))
        self.situation.ajouter_action(ActionPoker(Move.FOLD))
        self.situation.ajouter_action(ActionPoker(Move.RAISE_ALL_IN))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.situation.ajouter_action(ActionPoker(Move.CALL))
        self.assertFalse(self.situation.is_leaf(n_joueurs))
        self.situation.ajouter_action(ActionPoker(Move.CALL))

        self.assertTrue(self.situation.is_leaf(n_joueurs))



