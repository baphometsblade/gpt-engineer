from game_mechanics import Game
from cards import all_cards

def main():
    player1_deck = all_cards[:len(all_cards)//2]
    player2_deck = all_cards[len(all_cards)//2:]
    game_board = GameBoard(["player1_area", "player2_area"])
    tokens = [Token("health", 10), Token("points", 0)]
    rulebook = Rulebook("rules", "card_abilities", "special_moves")

    game = Game(player1_deck, player2_deck, game_board, tokens, rulebook)
    game.setup()

    while True:
        # Game loop
        pass

if __name__ == "__main__":
    main()