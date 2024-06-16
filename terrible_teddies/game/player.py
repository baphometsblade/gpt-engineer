class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.health_points = 10

    def draw_card(self, card):
        self.hand.append(card)

    def play_card(self, card):
        self.hand.remove(card)
        # Add logic to activate card ability

    def __str__(self):
        return f"{self.name} - Health Points: {self.health_points}"