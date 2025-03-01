# Describe Various Kinds Of Beverageware
from beverages import *


class Vessel:
    
    def __init__(self, volume: int, contents: Beverage | None) -> None:
        self.volume = volume
        self.contents = contents


class Glass:
    pass


class Bottle(Vessel):

    def __init__(self, volume: int, contents: Beverage | None) -> None:
        super().__init__(volume, contents)
        if self.contents:
            self.contents.amount = self.volume
            self.sealed = True

    @property
    def label(self):
        return f"{str(self.contents)} {self.volume} mL"

    def open(self):
        self.sealed = False
        #print(f"{telf.label} bottle was opened.")

    def pour(self, amount: int) -> Beverage:
        if self.sealed:
            raise AttributeError("The Bottle is sealed, cannot pour!")
        if amount > self.contents.amount:
            raise ValueError("Not enough contents!")
        self.contents.amount -= amount
        return type(self.contents)(**self.contents.get_properties(), amount=amount)

    def pour_in(self, beverage:Beverage, amount: int) -> None:
        if beverage.get_properties() != self.contents.get_properties():
            raise ValueError("Mixing beverages in Bottle is not allowed!")
        if self.contents.amount + amount > self.volume:
            raise ValueError("Contents amount cannot exceed volume of Bottle!")
        self.contents.amount += amount

    def get_contents_stock_props(self):
        beverage_props = self.contents.get_properties()
        contents_stock_props = {**beverage_props, **dict(amount=self.volume)}
        return contents_stock_props

    def __del__(self):
        del self.contents



class Keg:
    pass

