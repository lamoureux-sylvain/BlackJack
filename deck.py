class Deck:
    def __init__(self):
        self.deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards_value = {"J": 10, "Q": 10, "K": 10}

    def table_deck(self):
        self.played_deck = self.deck

    def distribution(self):
        pass