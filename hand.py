from cards import Card


class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        self.check_ace = False

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        if self.dealer:
            for card in self.cards:
                if card.value.isnumeric():
                    self.value += int(card.value)

                elif card.value == "A":
                    self.aces()

                else:
                    self.value += 10
        else:
            for card in self.cards:
                if card.value.isnumeric():
                    self.value += int(card.value)

                elif card.value == "A" and not self.check_ace:
                    if self.value <= 10:
                        self.aces()
                    else:
                        self.value += 1

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
                print()
            else:
                print(self.cards[0])
                print(self.cards[1])
                print("Valeur:", self.get_value())
                print()
        else:
            if self.dealer:
                for card in self.cards:
                    print(card)
                print("Valeur:", self.get_value())
                print()
            else:
                for card in self.cards:
                    print(card)
                print("Valeur:", self.get_value())
                print()

    def aces(self):
        if self.dealer:
            self.value += 11
            if self.value > 21:
                self.value -= 10

        else:
            if self.value == 10:
                self.value += 11
            else:
                self.ace_value = 0
                while self.ace_value != "1" and self.ace_value != "11":
                    self.ace_value = input("Valeur de l'As: 1 ou 11 : ")
                    print()
                self.check_ace = True
                self.value += int(self.ace_value)