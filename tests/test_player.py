import unittest
from unittest.mock import patch
from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Player 1")

    @patch('builtins.input', return_value='3')
    def test_rank_card(self, input_mock):
        card = Card("Card 1", 3)
        self.player.rank_card(card)
        self.assertEqual(self.player.score, 1)

if __name__ == "__main__":
    unittest.main()