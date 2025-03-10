import unittest
import random

from scraping.gtowizard import RangeGtoWizard


class TestPokerRangeGtoWizard(unittest.TestCase):
    def test_scrap_la_range_dans_le_bon_ordre(self):
        range_origine: dict[str, float] = {
            "22": random.uniform(0, 1),
            "32o": random.uniform(0, 1),
            "32s": random.uniform(0, 1),
            "33": random.uniform(0, 1),
            "42o": random.uniform(0, 1),
            "42s": random.uniform(0, 1),
            "43o": random.uniform(0, 1),
            "43s": random.uniform(0, 1),
            "44": random.uniform(0, 1),
            "52o": random.uniform(0, 1),
            "52s": random.uniform(0, 1),
            "53o": random.uniform(0, 1),
            "53s": random.uniform(0, 1),
            "54o": random.uniform(0, 1),
            "54s": random.uniform(0, 1),
            "55": random.uniform(0, 1),
            "62o": random.uniform(0, 1),
            "62s": random.uniform(0, 1),
            "63o": random.uniform(0, 1),
            "63s": random.uniform(0, 1),
            "64o": random.uniform(0, 1),
            "64s": random.uniform(0, 1),
            "65o": random.uniform(0, 1),
            "65s": random.uniform(0, 1),
            "66": random.uniform(0, 1),
            "72o": random.uniform(0, 1),
            "72s": random.uniform(0, 1),
            "73o": random.uniform(0, 1),
            "73s": random.uniform(0, 1),
            "74o": random.uniform(0, 1),
            "74s": random.uniform(0, 1),
            "75o": random.uniform(0, 1),
            "75s": random.uniform(0, 1),
            "76o": random.uniform(0, 1),
            "76s": random.uniform(0, 1),
            "77": random.uniform(0, 1),
            "82o": random.uniform(0, 1),
            "82s": random.uniform(0, 1),
            "83o": random.uniform(0, 1),
            "83s": random.uniform(0, 1),
            "84o": random.uniform(0, 1),
            "84s": random.uniform(0, 1),
            "85o": random.uniform(0, 1),
            "85s": random.uniform(0, 1),
            "86o": random.uniform(0, 1),
            "86s": random.uniform(0, 1),
            "87o": random.uniform(0, 1),
            "87s": random.uniform(0, 1),
            "88": random.uniform(0, 1),
            "92o": random.uniform(0, 1),
            "92s": random.uniform(0, 1),
            "93o": random.uniform(0, 1),
            "93s": random.uniform(0, 1),
            "94o": random.uniform(0, 1),
            "94s": random.uniform(0, 1),
            "95o": random.uniform(0, 1),
            "95s": random.uniform(0, 1),
            "96o": random.uniform(0, 1),
            "96s": random.uniform(0, 1),
            "97o": random.uniform(0, 1),
            "97s": random.uniform(0, 1),
            "98o": random.uniform(0, 1),
            "98s": random.uniform(0, 1),
            "99": random.uniform(0, 1),
            "A2o": random.uniform(0, 1),
            "A2s": random.uniform(0, 1),
            "A3o": random.uniform(0, 1),
            "A3s": random.uniform(0, 1),
            "A4o": random.uniform(0, 1),
            "A4s": random.uniform(0, 1),
            "A5o": random.uniform(0, 1),
            "A5s": random.uniform(0, 1),
            "A6o": random.uniform(0, 1),
            "A6s": random.uniform(0, 1),
            "A7o": random.uniform(0, 1),
            "A7s": random.uniform(0, 1),
            "A8o": random.uniform(0, 1),
            "A8s": random.uniform(0, 1),
            "A9o": random.uniform(0, 1),
            "A9s": random.uniform(0, 1),
            "AA": random.uniform(0, 1),
            "AJo": random.uniform(0, 1),
            "AJs": random.uniform(0, 1),
            "AKo": random.uniform(0, 1),
            "AKs": random.uniform(0, 1),
            "AQo": random.uniform(0, 1),
            "AQs": random.uniform(0, 1),
            "ATo": random.uniform(0, 1),
            "ATs": random.uniform(0, 1),
            "J2o": random.uniform(0, 1),
            "J2s": random.uniform(0, 1),
            "J3o": random.uniform(0, 1),
            "J3s": random.uniform(0, 1),
            "J4o": random.uniform(0, 1),
            "J4s": random.uniform(0, 1),
            "J5o": random.uniform(0, 1),
            "J5s": random.uniform(0, 1),
            "J6o": random.uniform(0, 1),
            "J6s": random.uniform(0, 1),
            "J7o": random.uniform(0, 1),
            "J7s": random.uniform(0, 1),
            "J8o": random.uniform(0, 1),
            "J8s": random.uniform(0, 1),
            "J9o": random.uniform(0, 1),
            "J9s": random.uniform(0, 1),
            "JJ": random.uniform(0, 1),
            "JTo": random.uniform(0, 1),
            "JTs": random.uniform(0, 1),
            "K2o": random.uniform(0, 1),
            "K2s": random.uniform(0, 1),
            "K3o": random.uniform(0, 1),
            "K3s": random.uniform(0, 1),
            "K4o": random.uniform(0, 1),
            "K4s": random.uniform(0, 1),
            "K5o": random.uniform(0, 1),
            "K5s": random.uniform(0, 1),
            "K6o": random.uniform(0, 1),
            "K6s": random.uniform(0, 1),
            "K7o": random.uniform(0, 1),
            "K7s": random.uniform(0, 1),
            "K8o": random.uniform(0, 1),
            "K8s": random.uniform(0, 1),
            "K9o": random.uniform(0, 1),
            "K9s": random.uniform(0, 1),
            "KJo": random.uniform(0, 1),
            "KJs": random.uniform(0, 1),
            "KK": random.uniform(0, 1),
            "KQo": random.uniform(0, 1),
            "KQs": random.uniform(0, 1),
            "KTo": random.uniform(0, 1),
            "KTs": random.uniform(0, 1),
            "Q2o": random.uniform(0, 1),
            "Q2s": random.uniform(0, 1),
            "Q3o": random.uniform(0, 1),
            "Q3s": random.uniform(0, 1),
            "Q4o": random.uniform(0, 1),
            "Q4s": random.uniform(0, 1),
            "Q5o": random.uniform(0, 1),
            "Q5s": random.uniform(0, 1),
            "Q6o": random.uniform(0, 1),
            "Q6s": random.uniform(0, 1),
            "Q7o": random.uniform(0, 1),
            "Q7s": random.uniform(0, 1),
            "Q8o": random.uniform(0, 1),
            "Q8s": random.uniform(0, 1),
            "Q9o": random.uniform(0, 1),
            "Q9s": random.uniform(0, 1),
            "QJo": random.uniform(0, 1),
            "QJs": random.uniform(0, 1),
            "QQ": random.uniform(0, 1),
            "QTo": random.uniform(0, 1),
            "QTs": random.uniform(0, 1),
            "T2o": random.uniform(0, 1),
            "T2s": random.uniform(0, 1),
            "T3o": random.uniform(0, 1),
            "T3s": random.uniform(0, 1),
            "T4o": random.uniform(0, 1),
            "T4s": random.uniform(0, 1),
            "T5o": random.uniform(0, 1),
            "T5s": random.uniform(0, 1),
            "T6o": random.uniform(0, 1),
            "T6s": random.uniform(0, 1),
            "T7o": random.uniform(0, 1),
            "T7s": random.uniform(0, 1),
            "T8o": random.uniform(0, 1),
            "T8s": random.uniform(0, 1),
            "T9o": random.uniform(0, 1),
            "T9s": random.uniform(0, 1),
            "TT": random.uniform(0, 1),
        }

        self.assertEqual(169, len(range_origine))

        range_gto_wizard: RangeGtoWizard = RangeGtoWizard([value for key, value in range_origine.items()])

        range_convertie = range_gto_wizard.to_dict()

        self.assertDictEqual(range_origine, range_convertie, "Mauvaise conversion")

