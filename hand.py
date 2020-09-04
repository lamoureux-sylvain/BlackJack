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
        if self.dealer:
            for card in self.cards:
                if card.value.isnumeric():
                    self.value += int(card.value)

                else:
                    if self.cards[0].value == "A":
                        self.value += 1
                    if self.cards[1].value == "A":
                        self.value += 11
                        if self.value > 21:
                            self.value -= 10

                    else:
                        self.value += 10
        else:
            for card in self.cards:
                if card.value.isnumeric():
                    self.value += int(card.value)

                else:
                    
                    if self.cards[0].value == "A":
                        while (self.ace_value != "1") and (self.ace_value != "11"):
                            self.ace_value = input(
                                "Quelle valeur donnez vous à l'As ? 1 ou 11 ?: "
                            )
                        self.value += int(self.ace_value)
                    if self.cards[1].value == "A":
                        if self.value == 10:
                            self.value = 11
                        else:
                            while (self.ace_value != "1") and (self.ace_value != "11"):
                                self.ace_value = input(
                                    "Quelle valeur donnez vous à l'As ? 1 ou 11 ?: "
                                )
                            self.value += int(self.ace_value)

                    else:
                        self.value += 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self, nb_card):
        self.nb_card = nb_card
        if self.nb_card <= 2:
            if self.dealer:
                print(self.cards[0])
                print("Carte cachée")
            else:
                print(self.cards[0])
                print(self.cards[1])
                print("Valeur:", self.get_value())
        else:
            if self.dealer:
                for card in self.cards:
                    print(card)
                print("Valeur:", self.get_value())
            else:
                for card in self.cards:
                    print(card)
                print("Valeur:", self.get_value())