class User:
    def __init__(self, players):
        self.nb_players = 1
        self.players = players
        self.player_token = 1000

    def generate_player(self):
        for number in range(self.nb_players):
            self.players.append(
                input("J" + str(number + 1) + "... Quel est votre pseudo ? ")
            )
        if len(self.players) == 1:
            print("Enchanté", self.players[0],"!")
            print("Pour fêter notre rencontre voici", self.player_token,"jetons !!")
            return User(self.players)
        else:
            print("Enchanté", ", ".join(self.players), "!")
            print("Pour fêter notre rencontre voici", self.player_token,"jetons !!")

if __name__ == "__main__":
    user = User([])
    user.generate_player()