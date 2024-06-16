from dataclasses import dataclass

@dataclass
class Player:
    """
    Represents a player in the game.
    """
    name: str
    score: int = 0

    def rank_card(self, card: 'Card'):
        rank = int(input(f"{self.name}, rank this card (1-5): "))
        if rank == card.rank:
            self.score += 1
        print(f"{self.name} scored {self.score} points so far.")