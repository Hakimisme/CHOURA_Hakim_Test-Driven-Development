import unittest
from poker.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_draw_cards(self):
        deck = Deck()
        drawn_cards = deck.draw(5)
        self.assertEqual(len(drawn_cards), 5)
        self.assertEqual(len(deck.cards), 47)

if __name__ == "__main__":
    unittest.main()