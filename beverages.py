from enum import Enum


class Beverage:
    def __init__(self, brand: str, variety: str, amount: int | None = None):
        self.amount = amount
        self.brand = brand
        self.variety = variety

    def get_amount(self):
        return self.amount

    def get_properties(self):
        pass

    def is_alcoholic(self):
        pass


class Fermented(Beverage):

    class Base(Enum):
        GRN = "Grain based"
        SGR = "Sugar based"
        FRT = "Fruit based"
        SPC = "Special starch based"

    def __init__(self, brand: str, variety: str, abv: float | int, amount: int | None = None):
        super().__init__(brand, variety, amount)
        self._abv = float(abv)

    @property
    def abv(self) -> float | int:
        return int(self._abv) if round(self._abv) == self._abv else self._abv

    def is_alcoholic(self):
        return True if self._abv > 0.5 else False

    def get_properties(self):
        pass


class Spirit(Fermented):

    class DistillType(Enum):
        PTS = "Pot Still Distillation"
        CLS = "Column Still Distillation"
        VCM = "Vacuum Distillation"
        HBR = "Hybrid Distillation"

    class DistillCount(Enum):
        SNG = "Single"
        DBL = "Double"
        TRP = "Triple"
        MLT = "Multiple"

    def __init__(self, brand: str, variety: str, abv: float | int, amount: int | None = None):
        super().__init__(brand, variety, abv, amount)

class Whiskey(Spirit):

    class Provenance(Enum):
        SCT = "Scotch"
        IRS = "Irish"
        BRB = "Bourbon"
        TNS = "Tennessee"
        CND = "Canadian"
        USA = "US"  # if not Bourbon or Tennessee ?
        IND = "Indian"
        AUS = "Australian"
        JAP = "Japanese"
        TAI = "Taiwanese"
        GRM = "German"

    class Style(Enum):
        SMW = "Single Malt"
        SGW = "Single Grain"
        BMW = "Blended Malt"
        BGW = "Blended Grain"
        BLW = "Blended"
        GRW = "Grain"
        SPS = "Single Pot Still"
        STR = "Straight"
        RYE = "Rye"  # for "Canadian Rye"
        SRY = "Straight Rye"
        SBR = "Single Barrel Rye"
        WHT = "Wheatened"
        SNB = "Single Barrel"
        CSK = "Cask Strength"

    def __init__(self,
                 brand: str,
                 variety: str,
                 provenance: Provenance,
                 style: Style,
                 abv: float | int = 40,
                 amount: int | None = None):
        super().__init__(brand, variety, abv, amount)
        self.base_substrate = Whiskey.Base.GRN
        self.provenance = provenance
        self.style = style

    def __repr__(self):
        return (
            f"Whiskey(brand={self.brand}, variety={self.variety}, provenance={self.provenance}, "
            f"style={self.style}, abv={self.abv}{', amount=' + str(self.amount) if self.amount else ''})"
        )

    def __str__(self):
        if self.provenance is Whiskey.Provenance.BRB:
            details = f"{self.style.value} {self.provenance.value}"
        elif self.provenance is Whiskey.Provenance.CND and self.style is Whiskey.Style.RYE:
            details = f"{self.provenance.value} {self.style.value}"
        else:
            details = f"{self.style.value} {self.provenance.value} Whiskey"
        return f"{self.brand} {self.variety} ({details})"

    def get_properties(self):
        return dict(
            brand=self.brand,
            variety=self.variety,
            provenance=self.provenance,
            style=self.style,
            abv=self.abv
        )


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








