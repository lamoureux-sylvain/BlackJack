from menu import Menu


class Bet:
    def __init__(self, player_token):
        self.player_token = player_token
        self.game_over = ""

    def drop_bet(self):
        self.table_bet = 0
        print("                       Vous avez", self.player_token, "jetons.")

        if self.player_token < 5:
            while self.game_over != "c":
                self.game_over = input("Vous n'avez plus assez de jeton !! (C)").lower()
            menu = Menu()
            menu.main_title()

        while (self.table_bet < 5) or (self.table_bet > self.player_token):
            self.table_bet = int(
                input("                     Combien voulez vous parier ? \n")
            )
            if self.table_bet < 5:
                print("Vous devez parier au moins 5 jetons...")
            elif self.table_bet > self.player_token:
                print("Vous n'avez pas cette quantité de jeton...")

        self.player_token -= self.table_bet
        print(
            r"""+===================================================================+ """
        )
        print("|                       Les jeux sont fait !!                       |")
        print(
            r"""+===================================================================+"""
        )
        return Bet(self.player_token)

    def black_jack_gain(self):
        self.player_token += self.table_bet * 3
        print("Vous triplez votre mise !!!!")
        print("Vous gagnez", self.table_bet * 3, "jetons !!")
        return Bet(self.player_token)

    def win_gain(self):
        self.player_token += self.table_bet * 2
        print("Vous doublez votre mise !!")
        print("Vous gagnez", self.table_bet * 2, "jetons !!")
        return Bet(self.player_token)
