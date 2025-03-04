import unittest
from poker.hand import PokerHand

class TestPokerHand(unittest.TestCase):
    def test_royal_flush(self):
        hand = PokerHand(["10♥", "J♥", "Q♥", "K♥", "A♥"])
        self.assertEqual(hand.evaluate_hand(), (9, "Quinte Flush Royale"))

    def test_straight_flush(self):
        hand = PokerHand(["9♠", "8♠", "7♠", "6♠", "5♠"])
        self.assertEqual(hand.evaluate_hand(), (8, "Quinte Flush"))

    def test_four_of_a_kind(self):
        hand = PokerHand(["7♠", "7♦", "7♣", "7♥", "9♦"])
        self.assertEqual(hand.evaluate_hand(), (7, "Carré"))

    def test_full_house(self):
        hand = PokerHand(["10♠", "10♦", "10♣", "4♥", "4♠"])
        self.assertEqual(hand.evaluate_hand(), (6, "Full"))

    def test_flush(self):
        hand = PokerHand(["A♣", "10♣", "7♣", "6♣", "2♣"])
        self.assertEqual(hand.evaluate_hand(), (5, "Couleur"))

    def test_straight(self):
        hand = PokerHand(["9♥", "8♣", "7♠", "6♦", "5♥"])
        self.assertEqual(hand.evaluate_hand(), (4, "Quinte"))

    def test_three_of_a_kind(self):
        hand = PokerHand(["8♥", "8♦", "8♠", "K♣", "3♦"])
        self.assertEqual(hand.evaluate_hand(), (3, "Brelan"))

    def test_two_pair(self):
        hand = PokerHand(["J♥", "J♣", "4♠", "4♥", "A♦"])
        self.assertEqual(hand.evaluate_hand(), (2, "Deux Paires"))

    def test_one_pair(self):
        hand = PokerHand(["10♥", "10♣", "K♠", "4♥", "3♦"])
        self.assertEqual(hand.evaluate_hand(), (1, "Paire"))

    def test_high_card(self):
        hand = PokerHand(["A♠", "K♦", "Q♣", "J♥", "9♠"])
        self.assertEqual(hand.evaluate_hand(), (0, "Carte Haute: A"))


if __name__ == "__main__":
    unittest.main()
