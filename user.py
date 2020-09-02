class User:
    def __init__(self, nb_players):
        self.nb_players = nb_players
        self.players = []

    def generate_player(self):
        for number in range(self.nb_players):
            self.players.append(
                input("J" + str(number + 1) + "... Quel est votre pseudo ? ")
            )
        if len(self.players) == 1:
            print("Enchanté", self.players)
            print("Pour fêter notre rencontre voici 100 jetons !!")
        else:
            print("Enchanté", ", ".join(self.players), "!")
            print("Pour fêter notre rencontre voici 100 jetons !!")

    def generate_gain(self, tokken):
        self.tokken = tokken

    def hand(self):
        self.card = []
        self.value = 0
