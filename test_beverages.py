import unittest

from beverages import *


class TestWhiskey(unittest.TestCase):
    def test_tennessee_bourbon(self):
        j_dan_old_no7 = Whiskey(
            brand = "Jack Daniel's",
            variety = "Old No.7",
            provenance = "Tennessee, US",
            style = "Straight Tennessee Whiskey"
        )
        self.assertEqual(str(j_dan_old_no7), "Jack Daniel's Old No.7 (Straight Tennessee Whiskey, Tennessee, US)")
        monkeyshoulder = Scotch(
            brand = "Monkey Shoulder",
            variety = "The Original",
            style = Scotch.Style.BDM
        )
        self.assertEqual(str(monkeyshoulder), "Monkey Shoulder The Original (Blended Malt Scotch Whisky)")


class TestFermented(unittest.TestCase):
    def test_abv_property(self):
        fermbev = Fermented("Brand", "Variety", 40)
        self.assertIsInstance(fermbev._abv, float)
        self.assertEqual(fermbev._abv, 40)
        self.assertIsInstance(fermbev.abv, int)
        self.assertEqual(fermbev.abv, 40)
        fermbev = Fermented("Brand", "Variety", 39.9)
        self.assertIsInstance(fermbev._abv, float)
        self.assertEqual(fermbev._abv, 39.9)
        self.assertIsInstance(fermbev.abv, float)
        self.assertEqual(fermbev.abv, 39.9)




