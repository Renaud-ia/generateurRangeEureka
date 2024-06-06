import json
import os
import unittest
from unittest.mock import MagicMock

from persistence.json_enregistreur import JsonEnregistreur, SituationPoker, RangePoker
from poker import InitialSymmetricStacks


class TestJsonEnregistreur(unittest.TestCase):
    def setUp(self):
        self.variante_poker = "Texas Hold'em"
        self.enregistreur = JsonEnregistreur(self.variante_poker)
        self.enregistreur.adresse_fichier = "test.json"
        self.enregistreur.donnees = {"statut": False}
        self.stacks = InitialSymmetricStacks(25)

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
        self.assertTrue(self.enregistreur.donnees["statut"])

    def test_ajouter_range(self):
        # Mock SituationPoker et RangePoker
        situation = SituationPoker(self.stacks)

        # Simuler le comportement de to_key()
        situation.to_key = MagicMock(return_value="test_key")

        poker_range = RangePoker()
        poker_range.to_dict = MagicMock({'AA': 0.6})

        # Ajouter une range
        result = self.enregistreur.ajouter_range(situation, poker_range)
        self.assertTrue(result)
        self.assertEqual(self.enregistreur.donnees["test_key"], poker_range.to_dict())

        # Ajouter la même range
        result = self.enregistreur.ajouter_range(situation, poker_range)
        self.assertFalse(result)

    def test_enregistrement_termine(self):
        # Vérifier le statut initial
        self.assertFalse(self.enregistreur.enregistrement_termine())

        # Fixer le statut et vérifier
        self.enregistreur._fixer_statut(True)
        self.assertTrue(self.enregistreur.enregistrement_termine())


if __name__ == '__main__':
    unittest.main()

