import unittest
from poker.game import PokerGame

class TestPokerGame(unittest.TestCase):
    def test_game_initialization(self):
        game = PokerGame(players=2)
        self.assertEqual(len(game.players), 2)
        for player in game.players:
            self.assertEqual(len(game.players[player].cards), 5)

if __name__ == "__main__":
    unittest.main()
