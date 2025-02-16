import unittest

from drinkware import *
from beverages import *
from shelf import Shelf


class TestShelf(unittest.TestCase):

    def test_shelf_bottle_take_bottle_pour_bottle(self):
        shlf = Shelf()
        bvrg = Whiskey("Monkey Shoulder", "The Original", Whiskey.Provenance.SCT, Whiskey.MashBill.BMW)
        bttl = Bottle(700, bvrg)
        # test if bottles shelved and bottle count is correct
        shlf.shelf_bottle(bttl, 2)
        self.assertEqual(
            shlf.whiskeys,
            {"Monkey Shoulder The Original (Scotch Blended Malt Whiskey)": {"item": bttl, "count": 2}}
        )
        # test if new bottle is full?
        self.assertEqual(
            shlf.whiskeys["Monkey Shoulder The Original (Scotch Blended Malt Whiskey)"]["item"].contents.amount,
            shlf.whiskeys["Monkey Shoulder The Original (Scotch Blended Malt Whiskey)"]["item"].volume
        )
        # test if bottle count increments correctly when more bottles shelved
        shlf.shelf_bottle(bttl, 1)
        self.assertEqual(
            shlf.whiskeys,
                {"Monkey Shoulder The Original (Scotch Blended Malt Whiskey)": {"item": bttl, "count": 3}}
        )
        # test if bottle count decrements correctly when bottle is taken from the shelf
        bottle = shlf.take_bottle("Monkey Shoulder The Original (Scotch Blended Malt Whiskey)")
        self.assertEqual(shlf.whiskeys["Monkey Shoulder The Original (Scotch Blended Malt Whiskey)"]["count"], 2)
        # test if bottle contents amount decrements correctly when pouring
        initial_amount = bottle.contents.amount
        bottle.pour(50)
        self.assertEqual(bottle.contents.amount, initial_amount - 50)
        # test if shelving a poured bottle remembers bottle contents amount
        shlf.shelf_bottle(bottle)  # also testing a default value for 'bottle_count' argument of class 'Bottle'
        self.assertEqual(shlf.whiskeys[bottle.label]["item"].contents.amount, initial_amount - 50)
        # test if raise ValueError in Shelf.shelf_bottle() works as expected
        bad_bottle = Bottle(700, Whiskey(bvrg.brand, bvrg.variety, bvrg.provenance, bvrg.mash_bill, 200))
        with self.assertRaises(ValueError):
            shlf.shelf_bottle(bad_bottle)










