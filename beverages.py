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

    #xi nastupni dva Enum-klasy – na maibutnee
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

    def __init__(self,
                 brand: str,
                 variety: str,
                 style: str | None = None,
                 provenance: str | None = None,
                 abv: float | int = 40,
                 amount: int | None = None):
        super().__init__(brand=brand, variety=variety, abv=abv, amount=amount)
        self.base_substrate = Spirit.Base.GRN
        self.style = style
        self.provenance = provenance

    def __repr__(self):
        return (
            f"Whiskey(brand={self.brand}, variety={self.variety}"
            f"{', style=' + self.style if self.style else ''}, abv={self.abv}"
            f"{', provenance=' + str(self.provenance) if self.provenance else ''}" 
            f"{', amount=' + str(self.amount) if self.amount else ''})"
        )

    def __str__(self):
        details = ", ".join([d for d in (self.style, self.provenance) if d is not None])
        return f"{self.brand} {self.variety}{' (' + details + ')' if details else ''}"

    def get_properties(self):
        return dict(
            brand=self.brand,
            variety=self.variety,
            provenance=self.provenance,
            style=self.style,
            abv=self.abv
        )


class Scotch(Whiskey):
    class Style(Enum):
        SNM = "Single Malt"
        SNG = "Single Grain"
        BDM = "Blended Malt"
        BDG = "Blended Grain"
        BLD = "Blended"

    def __init__(self,
                 brand: str,
                 variety: str,
                 style: Style,
                 provenance: str | None = "Scotland",
                 abv: float | int = 40,
                 amount: int | None = None):
        if provenance not in (None, "Scotland"):
            raise ValueError("Scotch is supposed to be from Scotland")
        super().__init__(brand=brand, variety=variety, abv=abv, amount=amount)
        self.provenance = "Scotland"
        self.style = style
    def __repr__(self):
        return (
            f"Scotch(brand={self.brand}, variety={self.variety}, provenance={self.provenance}, "
            f"style={self.style}, abv={self.abv}{', amount=' + str(self.amount) if self.amount else ''})"
        )

    def __str__(self):
        details = f"{self.style.value} Scotch Whisky"
        return f"{self.brand} {self.variety} ({details})"


class Irish(Whiskey):
    class Style(Enum):
        SNM = "Single Malt"
        SNP = "Single Pot Still"
        BDG = "Single Grain"
        BLD = "Blended"
        RSH = "Irish"
    pass

class Bourbon(Whiskey):
    class Style(Enum):
        TRD = "Traditional"
        HGR = "High-Rye"
        STR = "Straight"
        WHT = "Wheatened"
        SNB = "Single Barrel"
        CSK = "Cask Strength"
        BNB = "Bottle-In-Bond"
        BLN = "Blended"
        SMB = "Small Batch"
    pass


class Rye(Whiskey):
    pass


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








