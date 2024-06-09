import copy
import random

import json
import os
import unittest
from unittest.mock import MagicMock

from persistence.enregistreur import EntreeExisteDeja
from persistence.json_enregistreur import JsonEnregistreur, SituationPoker, RangePoker
from poker import InitialSymmetricStacks, ActionPoker, Move


class TestJsonEnregistreur(unittest.TestCase):
    def setUp(self):
        self.variante_poker = "Texas Hold'em"
        self.enregistreur = JsonEnregistreur(self.variante_poker)
        self.enregistreur.adresse_fichier = "test.json"
        self.enregistreur.donnees = {"termine": False}
        self.stacks = InitialSymmetricStacks(25.5)

        self.poker_range = RangePoker()
        self.poker_range.to_dict = MagicMock({'AA': 0.6})

        self.randoms_actions = [
            ActionPoker(Move.RAISE, 2.5),
            ActionPoker(Move.FOLD),
            ActionPoker(Move.CALL),
            ActionPoker(Move.RAISE_ALL_IN)
        ]

    def get_random_action(self):
        return random.choice(self.randoms_actions)

    def tearDown(self):
        if os.path.exists(self.enregistreur.adresse_fichier):
            os.remove(self.enregistreur.adresse_fichier)

    def test_charger_fichier_existant(self):
        # Créer un fichier test.json
        with open(self.enregistreur.adresse_fichier, 'w') as f:
            f.write('{"test": true}')

        # Charger le fichier
        donnees = self.enregistreur._charger_fichier(self.enregistreur.adresse_fichier)
        self.assertEqual(donnees, {"test": True})

    def test_charger_fichier_inexistant(self):
        # Charger un fichier inexistant
        donnees = self.enregistreur._charger_fichier(self.enregistreur.adresse_fichier)
        self.assertEqual(donnees, {})

    def test_fixer_statut(self):
        # Fixer le statut
        self.enregistreur._fixer_statut(True)
        self.assertTrue(self.enregistreur.donnees["termine"])

    def test_ajout_range(self):
        # Mock SituationPoker et RangePoker
        situation = SituationPoker(self.stacks)
        situation.ajouter_action(self.get_random_action())

        self.assertFalse(self.enregistreur.situation_deja_enregistree(situation))

        self.enregistreur.ajouter_range(situation, self.poker_range)
        self.assertTrue(self.enregistreur.situation_deja_enregistree(situation))

    def test_doublon_impossible(self):
        # Mock SituationPoker et RangePoker
        situation = SituationPoker(self.stacks)
        situation.ajouter_action(self.get_random_action())

        self.enregistreur.ajouter_range(situation, self.poker_range)

        with self.assertRaises(EntreeExisteDeja):
            self.enregistreur.ajouter_range(situation, self.poker_range)

    def test_enregistrement_termine(self):
        # Vérifier le statut initial
        self.assertFalse(self.enregistreur.deja_scrape())

        # Fixer le statut et vérifier
        self.enregistreur.terminer_enregistrement()
        self.assertTrue(self.enregistreur.deja_scrape())

    def test_situation_deja_scrapee(self):
        # Mock SituationPoker et RangePoker
        situation = SituationPoker(self.stacks)
        situation.ajouter_action(self.get_random_action())

        self.enregistreur.ajouter_range(situation, self.poker_range)

        situation_suivante = copy.deepcopy(situation)
        situation_suivante.ajouter_action(self.get_random_action())

        self.assertTrue(self.enregistreur.situation_deja_enregistree(situation))
        self.assertFalse(self.enregistreur.situation_deja_enregistree(situation_suivante))

    def test_impossible_enregistrer_situation_sans_action(self):
        # Mock SituationPoker et RangePoker
        situation = SituationPoker(self.stacks)

        with self.assertRaises(ValueError):
            self.enregistreur.ajouter_range(situation, self.poker_range)

    def test_on_genere_les_situations_suivantes_depuis_persistence_root(self):
        # Mock SituationPoker et RangePoker
        situation_initiale = SituationPoker(self.stacks)

        situations_posterieures: list[SituationPoker] = []

        for action in self.randoms_actions:
            situation_copie: SituationPoker = copy.deepcopy(situation_initiale)
            situation_copie.ajouter_action(action)

            situations_posterieures.append(situation_copie)
            self.enregistreur.ajouter_range(situation_copie, self.poker_range)

        print(situations_posterieures)

        situations: list[SituationPoker] = self.enregistreur.recuperer_situations_suivantes(situation_initiale)

        self.assertCountEqual(situations_posterieures, situations)

    def test_on_genere_les_situations_suivantes_depuis_persistence_non_root(self):
        # Mock SituationPoker et RangePoker
        situation_initiale = SituationPoker(self.stacks)

        for _ in range(random.randint(1, 5)):
            situation_initiale.ajouter_action(self.get_random_action())

        print(situation_initiale)

        situations_posterieures: list[SituationPoker] = []

        for action in self.randoms_actions:
            situation_copie: SituationPoker = copy.deepcopy(situation_initiale)
            situation_copie.ajouter_action(action)

            situations_posterieures.append(situation_copie)
            self.enregistreur.ajouter_range(situation_copie, self.poker_range)

        situations: list[SituationPoker] = self.enregistreur.recuperer_situations_suivantes(situation_initiale)

        print(situations)
        print(situations_posterieures)

        self.assertCountEqual(situations_posterieures, situations)


if __name__ == '__main__':
    unittest.main()

