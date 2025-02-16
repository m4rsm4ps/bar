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

    @property
    def label(self):
        return str(self.contents)

    def pour(self, amount: int) -> None:
        if amount > self.contents.amount:
            raise ValueError("Not enough booze!")
        self.contents.amount -= amount

    def pour_in(self, amount: int) -> None:
        if self.content.amount + amount > self.volume:
            raise ValueError("It's too much booze for this bottle!")
        self.contents.amount += amount



class Keg:
    pass

