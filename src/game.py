from dataclasses import dataclass
from random import shuffle
from typing import List

from .card import Card
from .player import Player

@dataclass
class Game:
    """
    Represents the game state.
    """
    cards: List[Card]
    players: List[Player]
    current_player: int

    def __post_init__(self):
        shuffle(self.cards)

    def play_round(self):
        card = self.cards.pop()
        print(f"Current Card: {card.text}")
        for player in self.players:
            player.rank_card(card)
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_game(self):
        while self.cards:
            self.play_round()
        self.determine_winner()

    def determine_winner(self):
        winner = max(self.players, key=lambda player: player.score)
        print(f"Winner: {winner.name} with a score of {winner.score}")