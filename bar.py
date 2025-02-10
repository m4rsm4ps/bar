# An Attempt To Model Drinks Using OOP


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


class Beverage:
    def __init__(self, amount : int):
        self.amount = amount


class Glass:
    pass


class Garnish:
    pass


class Bottle:
    pass


class Keg:
    pass

