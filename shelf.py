# Here We Keep The Actual Beverages

from drinkware import Bottle
from beverages import *


whiskeys = [
    ("Monkey Shoulder", "The Original", Whiskey.Provenance.SCT, Whiskey.MashBill.BMW),
]

freshes = [
    ("Housemade", "Genuine", Fresh.SourceCrop.LEMON),
]

syrups = [
    ("Housemade", "Sugar Syrup")
]

foamers = [
    ("Foam Mix", "...", Foamer.Origin.VEGAN),
]


class Shelf:

    def __init__(self) -> None:
        self.whiskeys = {}
        self.freshes = {}
        self.syrups = {}
        self.foamers = {}

    def shelf_bottle(self, bottle: Bottle, bottle_count: int = 1) -> None:
        if isinstance(bottle.contents, Whiskey):
            category = self.whiskeys
        elif isinstance(bottle.contents, Fresh):
            category = self.freshes
        elif isinstance(bottle.contents, Syrup):
            category = self.syrups
        elif isinstance(bottle.contents, Foamer):
            category = self.foamers
        if not category:
            category[bottle.label] = {"item": bottle, "count": bottle_count}
        else:
            if bottle.contents.amount < bottle.volume:
                if category[bottle.label]["item"].contents.amount < bottle.volume:
                    raise ValueError("Bottle on Shelf and Bottle in Hand are both not full!")
                del category[bottle.label]["item"]
                category[bottle.label]["item"] = bottle
            category[bottle.label]["count"] += 1

    def take_bottle(self, label: str) -> Bottle:
        shelf_contents = self.__dict__.values()
        for category in shelf_contents:
            if label in category.keys():
                bottle = category[label]["item"]
                category[label]["count"] -= 1
            if category[label]["count"] == 0:
                del category[label]
            else:
                contents_props = bottle.contents.__dict__
                contents_props["amount"] = bottle.volume
                category[label]["item"] = Bottle(
                    bottle.volume,
                    type(bottle.contents)(**contents_props)
                )
            return bottle














