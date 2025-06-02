# Here We Keep The Actual Beverages

from drinkware import Bottle
from beverages import *

class Shelf:

    def __init__(self) -> None:
        self.shelved = {}

    def shelf_bottle(self, bottle: Bottle , bottle_count: int = 1) -> None:
        if not bottle.label in self.shelved:
            self.shelved[bottle.label] = {
                "specs": {"type": type(bottle.contents), "properties": bottle.get_contents_stock_props()}
            }
        if bottle.sealed:
            try:
                self.shelved[bottle.label]["sealed"] += bottle_count
            except (KeyError, TypeError):
                self.shelved[bottle.label]["sealed"] = bottle_count
        elif not bottle.sealed:
            if bottle_count > 1:
                raise ValueError("Shelving several unsealed bottles is not allowed!")
            try:
                ready = self.shelved[bottle.label]["ready"]
                if not ready.sealed:  #AttributeError here if ready is None?
                    raise ValueError("Shelving several unsealed bottles is not allowed!")
                del self.shelved[bottle.label]["ready"]
                self.shelved[bottle.label]["sealed"] += 1
            except (KeyError, AttributeError):
                pass
            self.shelved[bottle.label]["ready"] = bottle

    def take_bottle(self, label: str) -> Bottle:
        if not label in self.shelved:
            raise ValueError("Invalid item name.")
        if not self.shelved[label].get("ready"):
            if not self.shelved[label].get("sealed"):
                raise ValueError(f"Not enough {label} on the shelf.")
            beverage = self.shelved[label]["specs"]
            beverage = beverage["type"](**beverage["properties"])
            new_sealed_bottle = Bottle(beverage.amount, beverage)
            self.shelved[label]["sealed"] = (
                None
                if self.shelved[label]["sealed"] - 1 == 0
                else self.shelved[label]["sealed"] - 1
            )
            self.shelved[label]["ready"] = new_sealed_bottle
        bottle = self.shelved[label]["ready"]
        self.shelved[label]["ready"] = None
        return bottle

    def list_all_items(self) -> list[tuple]:
        res = []
        for label in self.shelved:
            millilitres = self.get_mL(label)
            try:
                sealed = int(self.shelved[label].get("sealed"))
            except TypeError:
                sealed = 0
            bottle_count = sealed if not self.shelved[label].get("ready") else sealed + 1
            res.append((label, bottle_count, millilitres))
        return res

    def get_mL(self, label: str) -> int:
        try:
            label = self.shelved[label]
        except KeyError:
            raise ValueError("Invalid item name.")
        ready, sealed = label.get("ready"), label.get("sealed")
        if not ready:
            ready = 0
        else:
            ready = ready.contents.amount
        if not sealed:
            sealed = 0
        else:
            sealed = sealed * label["specs"]["properties"]["amount"]
        return ready + sealed

    def get_litres(self, label):
        return self.get_mL(label) / 1000











