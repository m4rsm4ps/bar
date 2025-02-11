import unittest

from beverages import Whiskey


class TestWhiskey(unittest.TestCase):
    def test_tennessee_bourbon(self):
        j_dan_old_no7 = Whiskey(
            brand = "Jack Daniel's",
            variety = "Old No.7",
            provenance = Whiskey.Provenance.TNS,
            mash_bill = Whiskey.MashBill.TNS
        )
        self.assertEqual(str(j_dan_old_no7), "Jack Daniel's Old No.7 (Tennessee Whiskey)")
        monkeyshoulder = Whiskey(
            brand = "Monkey Shoulder",
            variety = "The Original",
            provenance = Whiskey.Provenance.SCT,
            mash_bill = Whiskey.MashBill.BMW
        )
        self.assertEqual(str(monkeyshoulder), "Monkey Shoulder The Original (Scotch Blended Malt Whiskey)")

