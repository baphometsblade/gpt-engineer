import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_card_init(self):
        card = Card("Card 1", 3)
        self.assertEqual(card.text, "Card 1")
        self.assertEqual(card.rank, 3)

if __name__ == "__main__":
    unittest.main()