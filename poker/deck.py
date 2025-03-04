import random

class Deck:
    suits = ['♥', '♦', '♠', '♣']  
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  

    def __init__(self):
        self.cards = [f"{rank}{suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards) 

    def draw(self, n=1):
        return [self.cards.pop() for _ in range(n)] if len(self.cards) >= n else []

if __name__ == "__main__":
    deck = Deck()
    print(deck.draw(5)) 
