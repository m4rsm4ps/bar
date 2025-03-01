import unittest

from drinkware import *
from beverages import *
from shelf import Shelf


class TestShelf(unittest.TestCase):
    def setUp(self):
        self.beverage = Whiskey("Monkey Shoulder", "The Original", Whiskey.Provenance.SCT, Whiskey.MashBill.BMW)
        self.bottle = Bottle(700, self.beverage)

    def test_shelf_bottle(self):
        # test if bottles are shelved and bottle count is correct
        shelf = Shelf()
        bottle = self.bottle
        shelf.shelf_bottle(bottle, 2)
        #print(shelf.shelved[bottle.label])
        self.assertEqual(
            shelf.shelved[bottle.label],
            {
                "specs": {
                    "type": type(bottle.contents),
                    "properties": {**bottle.contents.get_properties(), **{"amount": 700}}
                },
                "sealed": 2,
            }
        )

    def test_only_single_unsealed_bottle_allowed(self):
        shelf = Shelf()
        bottle = self.bottle
        bottle.open()
        bottle.pour(1)
        with self.assertRaises(ValueError):
            shelf.shelf_bottle(bottle, 2)

    def test_sealed_bottle_count_increment(self):
        shelf = Shelf()
        bottle = self.bottle
        shelf.shelf_bottle(bottle, 1)
        self.assertEqual(shelf.shelved[bottle.label]["sealed"], 1)
        shelf.shelf_bottle(bottle, 665)
        self.assertEqual(shelf.shelved[bottle.label]["sealed"], 666) 
        bottle.open()
        bottle.pour(1)
        shelf.shelf_bottle(bottle)
        self.assertEqual(shelf.shelved[bottle.label]["sealed"], 666) 

    def test_take_bottle(self):
        shelf = Shelf()
        shelf.shelf_bottle(self.bottle, 2)
        taken = shelf.take_bottle(self.bottle.label)
        # test if sealed count decrements properly
        self.assertEqual(shelf.shelved[taken.label]["sealed"], 1)
        # test if sealed count takes value 'None' when depleted to zero
        self.assertIsNone(shelf.shelved[taken.label]["ready"])
        # test if raises when invalid value is passed
        with self.assertRaises(ValueError):
            shelf.take_bottle("Invalid Label")
        # test if raises when shelved items depleted
        next_taken = shelf.take_bottle(taken.label)
        with self.assertRaises(ValueError):
            shelf.take_bottle(next_taken.label)

    def test_take_and_shelf(self):
        shelf = Shelf()
        shelf.shelf_bottle(self.bottle)
        taken = shelf.take_bottle(self.bottle.label)
        self.assertIsNone(shelf.shelved[taken.label]["sealed"])
        shelf.shelf_bottle(taken)
        self.assertEqual(shelf.shelved[taken.label]["sealed"], 1)
        self.assertIsNone(shelf.shelved[taken.label]["ready"])
        taken.open()
        taken.pour(1)
        shelf.shelf_bottle(taken)
        self.assertIsNotNone(shelf.shelved[taken.label]["ready"])
        self.assertIs(taken, shelf.shelved[self.bottle.label]["ready"])
        self.assertEqual(shelf.shelved[taken.label]["ready"].contents.amount, taken.volume - 1)

    def test_get_mL_and_litres(self):
        shelf = Shelf()
        shelf.shelf_bottle(self.bottle)
        with self.assertRaises(ValueError):
            shelf.get_mL("Bad")
        self.assertEqual(shelf.get_mL(self.bottle.label), 700)
        taken = shelf.take_bottle(self.bottle.label)
        self.assertEqual(shelf.get_mL(self.bottle.label), 0)
        taken.open()
        shelf.shelf_bottle(taken)
        self.assertEqual(shelf.get_mL(self.bottle.label), 700)
        taken = shelf.take_bottle(self.bottle.label)
        taken.pour(334)
        shelf.shelf_bottle(taken)
        shelf.shelf_bottle(self.bottle, 9)
        self.assertEqual(shelf.get_mL(self.bottle.label), 6666)
        self.assertEqual(shelf.get_litres(self.bottle.label), 6.666)

    def test_list_all_items(self):
        shelf = Shelf()
        shelf.shelf_bottle(self.bottle, 9)
        self.bottle.open()
        self.bottle.pour(334)
        shelf.shelf_bottle(self.bottle)
        another = Bottle(1000, Whiskey("Jack Daniel's", "Old No.7", Whiskey.Provenance.TNS, Whiskey.MashBill.TNS))
        shelf.shelf_bottle(another, 2)
        another.open()
        another.pour(975)
        shelf.shelf_bottle(another)
        self.assertListEqual(
            shelf.list_all_items(),
            [
                ("Monkey Shoulder The Original (Scotch Blended Malt Whiskey) 700 mL", 10, 6666),
                ("Jack Daniel's Old No.7 (Tennessee Whiskey) 1000 mL", 3, 2025)
            ]
        )



















