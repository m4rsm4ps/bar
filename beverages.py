from enum import Enum


class Beverage:
    def __init__(self, brand: str, variety: str, amount: int | None = None):
        self.amount = amount
        self.brand = brand
        self.variety = variety

    def get_amount(self):
        return self.amount


class Whiskey(Beverage):

    class Provenance(Enum):
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
        WTW = "Wheat Whiskey"
        CRW = "Corn Whiskey"
        TNS = "Tennessee Whiskey"
        PSW = "Pot Still Whiskey"
        NTW = "Not Technically Whiskey"

    def __init__(self, brand: str, variety: str, provenance: Provenance, mash_bill: MashBill, amount: int | None = None):
        super().__init__(brand, variety, amount)
        self.provenance = provenance
        self.mash_bill = mash_bill

    def __repr__(self):
        return (
            f"Whiskey(brand={self.brand}, variety={self.variety}, provenance={self.provenance}, "
            f"mash_bill={self.mash_bill}{', amount=' + str(self.amount) if self.amount else ''})"
        )

    def __str__(self):
        if self.provenance in (Whiskey.Provenance.BRB, Whiskey.Provenance.TNS):
            details = self.mash_bill.value
        else:
            details= f"{self.provenance.value} {self.mash_bill.value}"
        return f"{self.brand} {self.variety} ({details})"


class Fresh(Beverage):

    class SourceCrop(Enum):
        LIME = "Fresh Lime Juice"
        LEMON = "Fresh Lemon Juice"

    def __init__(self, brand: str, variety: str, source_crop: SourceCrop, amount: int | None = None):
        super().__init__(brand, variety, amount)
        self.crop = crop

    def __repr__(self):
        return f"Fresh(brand={self.brand}, variety={self.variety}, source_crop={self.source_crop})"

    def __str__(self):
        return f"{self.brand} {self.variety} ({self.source_crop.value})"


class Syrup(Beverage):

    def __init__(self, brand: str, variety: str, amount: int | None = None):
        super().__init__(brand, variety, amount)

    def __repr__(self):
        return f"Syrup(brand={self.brand}, variety={self.variety}"

    def __str__(self):
        return f"{self.brand} {self.variety}"


class Foamer(Beverage):

    class Origin(Enum):
        VEGAN = "Synthesized or Pland-based Foamer"
        NONVEG = "Animal-derived Foamer"

    def __init__(self, brand: str, variety: str, origin: Origin, amount: int | None = None):
        super().__init__(brand, variety, amount)
        self.origin = origin

        def __repr__(self):
            return f"Foamer(brand={self.brand}, variety={self.variety} origin={self.origin})"

        def __str__(self):
            return f"{self.brand} {self.variety} ({self.origin})"








