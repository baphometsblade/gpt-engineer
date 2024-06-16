from dataclasses import dataclass

@dataclass
class PersonalizationOption:
    """Represents a personalization option."""
    name: str
    price: float

class Engraving(PersonalizationOption):
    """Represents an engraving personalization option."""
    def __init__(self):
        super().__init__(name="Engraving", price=0)

class LeatherSleeve(PersonalizationOption):
    """Represents a leather sleeve personalization option."""
    def __init__(self):
        super().__init__(name="Leather Sleeve & Charm", price=55)