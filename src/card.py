from dataclasses import dataclass

@dataclass
class Card:
    """
    Represents a card in the game.
    """
    text: str
    rank: int