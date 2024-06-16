import unittest
from unittest.mock import patch
from src.game import Game
from src.card import Card
from src.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.cards = [Card("Card 1", 3), Card("Card 2", 2)]
        self.players = [Player("Player 1"), Player("Player 2")]
        self.game = Game(self.cards, self.players, 0)

    @patch('builtins.input', return_value='3')
    def test_play_round(self, input_mock):
        self.game.play_round()
        self.assertEqual(self.game.cards, [Card("Card 2", 2)])

    def test_determine_winner(self):
        self.players.score = 2
        self.players.score = 1
        self.game.determine_winner()
        self.assertEqual(self.game.players.score, 2)

if __name__ == "__main__":
    unittest.main()