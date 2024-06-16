class Rulebook:
    def __init__(self):
        self.rules = {
            "setup": "Each player draws a hand of cards from their deck.",
            "turns": "Players take turns playing cards from their hand, activating abilities, and attacking their opponent's teddy bears.",
            "strategy": "Players must use a combination of offensive and defensive strategies, leveraging the unique abilities of their teddy bears to gain the upper hand.",
            "humor": "The game is infused with adult, tongue-in-cheek humor.",
            "winning_conditions": "The game continues until one player successfully depletes their opponent's health points or achieves a specific strategic objective outlined in the rulebook."
        }

    def get_rule(self, rule_name):
        return self.rules.get(rule_name)