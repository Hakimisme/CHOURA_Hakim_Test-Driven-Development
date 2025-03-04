class PokerHand:
    def __init__(self, cards):
        self.cards = cards
        self.ranks = sorted([c[:-1] for c in cards], key=self.rank_value, reverse=True)
        self.suits = [c[-1] for c in cards]

    def rank_value(self, rank):
        values = {str(i): i for i in range(2, 11)}
        values.update({"J": 11, "Q": 12, "K": 13, "A": 14})
        return values[rank]

    def evaluate_hand(self):
        if self.is_royal_flush(): return (9, "Quinte Flush Royale")
        if self.is_straight_flush(): return (8, "Quinte Flush")
        if self.is_four_of_a_kind(): return (7, "Carré")
        if self.is_full_house(): return (6, "Full")
        if self.is_flush(): return (5, "Couleur")
        if self.is_straight(): return (4, "Quinte")
        if self.is_three_of_a_kind(): return (3, "Brelan")
        if self.is_two_pair(): return (2, "Deux Paires")
        if self.is_one_pair(): return (1, "Paire")
        return (0, f"Carte Haute: {self.ranks[0]}")

    def is_flush(self):
        return len(set(self.suits)) == 1

    def is_straight(self):
        values = [self.rank_value(r) for r in self.ranks]
        return sorted(values) == list(range(min(values), max(values) + 1))

    def is_royal_flush(self):
        return self.is_flush() and set(self.ranks) == {"10", "J", "Q", "K", "A"}

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_four_of_a_kind(self):
        return any(self.ranks.count(r) == 4 for r in self.ranks)

    def is_full_house(self):
        return self.is_three_of_a_kind() and self.is_one_pair()

    def is_three_of_a_kind(self):
        return any(self.ranks.count(r) == 3 for r in self.ranks)

    def is_two_pair(self):
        return len(set(r for r in self.ranks if self.ranks.count(r) == 2)) == 2

    def is_one_pair(self):
        return len(set(r for r in self.ranks if self.ranks.count(r) == 2)) == 1

def get_hand_score(cards):
    hand = PokerHand(cards)
    return hand.evaluate_hand()


if __name__ == "__main__":
    input_cards = input("Entrez 5 cartes (ex: '10♥ J♥ Q♥ K♥ A♥'): ").split()
    score, description = get_hand_score(input_cards)
    print(f"Score: {score} - {description}")
