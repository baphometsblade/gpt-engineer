from dataclasses import dataclass

@dataclass
class Card:
    name: str
    ability: str
    description: str

    def __str__(self):
        return f"{self.name}: {self.ability} - {self.description}"

# Example Cards
sir_fluffington = Card("Sir Fluffington", "High Society", "A noble teddy bear with a monocle and top hat.")
lady_snugglebottom = Card("Lady Snugglebottom", "Cuddle Attack", "A seductive teddy bear whose Cuddle Attack can disarm even the fiercest opponent.")
baron_von_growl = Card("Baron Von Growl", "Roar of Doom", "A fierce warrior bear with the Roar of Doom ability, which can deal significant damage to multiple enemy bears.")