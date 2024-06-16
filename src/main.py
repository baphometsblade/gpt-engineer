from .game import Game
from .card import Card
from .player import Player

def main():
    cards = [Card("Card 1", 3), Card("Card 2", 2), Card("Card 3", 5), Card("Card 4", 1), Card("Card 5", 4)]
    players = [Player("Player 1"), Player("Player 2")]
    game = Game(cards, players, 0)
    game.play_game()

if __name__ == "__main__":
    main()