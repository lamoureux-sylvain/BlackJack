from cards import Card


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        self.ace_value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        # has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)

            else:
                if card.value == "A":
                    while (self.ace_value != "1") and (self.ace_value != "11"):
                        self.ace_value = input(
                            "Quelle valeur donnez vous à l'As ? 1 ou 11 ?: "
                        )
                    self.value += int(self.ace_value)

                else:
                    self.value += 10

        # if has_ace and self.value > 21:
        #     self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print("carte cachée")
            print(self.cards[0])
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())