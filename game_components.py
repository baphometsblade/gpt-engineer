from dataclasses import dataclass

@dataclass
class TeddyBear:
    name: str
    ability: str
    description: str

@dataclass
class GameBoard:
    player_areas: list

@dataclass
class Token:
    type: str
    value: int

@dataclass
class Rulebook:
    rules: str
    card_abilities: str
    special_moves: str