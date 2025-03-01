import unittest

from drinkware import *
from beverages import *


class TestBottle(unittest.TestCase):
    def setUp(self):
        self.monkey_shoulder = Whiskey(
            "Monkey Shoulder",
            "The Original",
            Whiskey.Provenance.SCT,
            Whiskey.MashBill.BMW
        )
        self.jack_daniels = Whiskey(
            "Jack Daniel's",
            "Old No.7",
            Whiskey.Provenance.TNS,
            Whiskey.MashBill.TNS
        )

    def test_new_bottle_is_sealed_and_full(self):
        # even if beverage has "amount" set, it won't affect the new bottle contents amount
        self.jack_daniels.amount = 1
        jack_bottle = Bottle(1000, self.jack_daniels)
        self.assertIs(jack_bottle.sealed, True)
        self.assertEqual(jack_bottle.contents.amount, jack_bottle.volume)

    def test_bottle_label(self):
        jack_bottle = Bottle(1000, self.jack_daniels)
        self.assertEqual(
            jack_bottle.label,
            "Jack Daniel's Old No.7 (Tennessee Whiskey) 1000 mL"
        )

    def test_open(self):
        jack_bottle = Bottle(1000, self.jack_daniels)
        jack_bottle.open()
        self.assertIs(jack_bottle.sealed, False)

    def test_pour(self):
        jack_bottle = Bottle(1000, self.jack_daniels)
        with self.assertRaises(AttributeError):
            jack_bottle.pour(0)
        jack_bottle.open()
        poured = jack_bottle.pour(50)
        self.assertIsInstance(poured, Whiskey)
        self.assertEqual(poured.amount, 50)
        self.assertEqual(jack_bottle.contents.amount, 950)
        with self.assertRaises(ValueError):
            jack_bottle.pour(1000)

    def test_pour_in(self):
        jack_bottle = Bottle(1000, self.jack_daniels)
        with self.assertRaises(ValueError) as er:
            jack_bottle.pour_in(self.jack_daniels, 1)
            self.assertIn("volume", er.exception.args[0])
        jack_bottle.open()
        jack_bottle.pour(100)
        with self.assertRaises(ValueError) as er:
            jack_bottle.pour_in(self.monkey_shoulder, 100)
            self.assertIn("Mixing", er.exception.args[0])

    def test_get_contents_stock_props(self):
        jack_bottle = Bottle(1000, self.jack_daniels)
        props = jack_bottle.get_contents_stock_props()
        self.assertIsInstance(props, dict)
        self.assertDictEqual(
            props,
            {
                "brand": "Jack Daniel's",
                "variety": "Old No.7",
                "provenance": Whiskey.Provenance.TNS,
                "mash_bill": Whiskey.MashBill.TNS,
                "amount": 1000
            }
        )







