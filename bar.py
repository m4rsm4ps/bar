# An Attempt To Model Drinks Using OOP

from beverages import *
from garnish import *
from drinkware import *


class Bar:
    pass


class Menu:
    pass


class Drink:
    def __init__(
        self,
        beverages : list[Beverage],
        glass : Glass | Bottle,
        garnishes : list[Garnishes] | None = None
    ):
        self.beverages = beverages
        self.glass = glass
        self.garnishes = garnishes


