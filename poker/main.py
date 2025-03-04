from poker.game import PokerGame

if __name__ == "__main__":
    num_players = int(input("Entrez le nombre de joueurs: "))
    game = PokerGame(players=num_players)
    game.play()
