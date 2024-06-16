class Token:
    def __init__(self, type):
        self.type = type
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def __str__(self):
        return f"{self.type} Token: {self.value}"