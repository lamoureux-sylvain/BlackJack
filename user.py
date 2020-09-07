class User:
    def __init__(self, players):
        self.nb_players = 1
        self.players = players

    def generate_player(self):
        for number in range(self.nb_players):
            print(
                r"""+===================================================================+ """
            )
            self.players.append(
                input("J" + str(number + 1) + "... Quel est votre pseudo ? ")
            )
        if len(self.players) == 1:

            print(
                r"""+-------------------------------------------------------------------+"""
            )
            print("\n                          Enchanté", self.players[0], "!")
            print("           Pour fêter notre rencontre voici 1000 jetons !\n")
            print(
                r"""+-------------------------------------------------------------------+"""
            )

            return User(self.players)
        else:
            print("Enchanté", ", ".join(self.players), "!")
            print("Pour fêter notre rencontre voici 1000 jetons !!")


if __name__ == "__main__":
    user = User([])
    user.generate_player()