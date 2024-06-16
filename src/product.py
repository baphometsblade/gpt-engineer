from dataclasses import dataclass

@dataclass
class Product:
    """Represents a product."""
    name: str
    description: str
    size: str
    price: float
    return_policy: str

@dataclass
class Fragrance(Product):
    """Represents a fragrance product."""
    notes: dict

class TerribleTeddy(Fragrance):
    """Represents the Terrible Teddy perfume."""
    def __init__(self):
        super().__init__(
            name="Terrible Teddy",
            description="A smooth operator, his sights are trained on Helen... until he meets the Duke.",
            size="75 ml",
            price=315.0,
            return_policy="90-day returns",
            notes={
                "base_notes": ["Ambroxan"],
                "head_notes": ["Incense"],
                "heart_notes": ["Leather"]
            }
        )