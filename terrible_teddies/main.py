from game.card import sir_fluffington, lady_snugglebottom, baron_von_growl
from game.game_board import GameBoard
from game.player import Player
from game.rulebook import Rulebook
from game.soundtrack import Soundtrack
from game.token import Token

def main():
    game_board = GameBoard()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1.draw_card(sir_fluffington)
    player1.draw_card(lady_snugglebottom)
    player2.draw_card(baron_von_growl)

    soundtrack = Soundtrack()
    soundtrack.play_track("Orchestral Track 1")

    rulebook = Rulebook()
    print(rulebook.get_rule("setup"))

    game_board.add_card(1, sir_fluffington)
    game_board.add_card(2, baron_von_growl)

    print(game_board)

if __name__ == "__main__":
    main()