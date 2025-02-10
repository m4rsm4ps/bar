from enum import Enum


class Beverage:
    def __init__(self, brand: str, variety: str, amount : int | None = None):
        self.amount = amount
        self.brand = brand
        self.variety = variety


class Whiskey(Beverage):

    class Origin(Enum):
        SCT = "Scotch"
        IRS = "Irish"
        BRB = "Bourbon"
        TNS = "Tennessee"
        JAP = "Japanese"
        CND = "Canadian"
        IND = "Indian"
        AUS = "Australian"
        TAI = "Taiwanese"
        GRM = "German"

    class MashBill(Enum):
        SMW = "Single Malt Whiskey"
        SGW = "Single Grain Whiskey"
        BMW = "Blended Malt Whiskey"
        BGW = "Blended Grain Whiskey"
        BLW = "Blended Whiskey"
        BRB = "Bourbon"
        RYE = "Rye Whiskey"
        WHW = "Wheat Whiskey"
        CRW = "Corn Whiskey"
        TNS = "Tennessee Whiskey"
        PSW = "Pot Still Whiskey"
        NTW = "Not Technically Whiskey"

    def __init__(self, brand: str, variety: str, origin: Origin, mash_bill: MashBill, amount: int | None = None):
        super().__init__(brand, variety, amount)
        self.origin = origin
        self.mash_bill = mash_bill

    def __str__(self):
        if self.origin in (Whiskey.Origin.BRB, Whiskey.Origin.TNS):
            details = self.mash_bill.value
        else:
            details = f"{self.origin.value} {self.mash_bill.value}"
        return f"{self.brand} {self.variety} ({details})"



if __name__ == "__main__":
    jack_daniels_old_no_7 = Whiskey(
        brand = "Jack Daniel's",
        variety = "Old No.7",
        origin = Whiskey.Origin.TNS,
        mash_bill = Whiskey.MashBill.TNS
    )


