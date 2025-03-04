from poker.deck import Deck
from poker.hand import PokerHand

class PokerGame:
    def __init__(self, players=2):
        self.deck = Deck()
        self.players = {f"Joueur {i+1}": PokerHand(self.deck.draw(5)) for i in range(players)}

    def play(self):
        results = {}
        for player, hand in self.players.items():
            rank, desc = hand.evaluate_hand()
            results[player] = (rank, desc, hand.cards)
            print(f"{player}: {', '.join(hand.cards)} => {desc}")

        winner = max(results, key=lambda x: results[x][0])
        print(f"\n🏆 {winner} remporte la partie avec {results[winner][1]} !")

if __name__ == "__main__":
    num_players = int(input("Entrez le nombre de joueurs: "))
    game = PokerGame(players=num_players)
    game.play()
