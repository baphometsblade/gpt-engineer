class GameBoard:
    def __init__(self):
        self.player1_area = []
        self.player2_area = []

    def add_card(self, player, card):
        if player == 1:
            self.player1_area.append(card)
        elif player == 2:
            self.player2_area.append(card)

    def remove_card(self, player, card):
        if player == 1:
            self.player1_area.remove(card)
        elif player == 2:
            self.player2_area.remove(card)

    def __str__(self):
        return f"Player 1 Area: {self.player1_area}\nPlayer 2 Area: {self.player2_area}"