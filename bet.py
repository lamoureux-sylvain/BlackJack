from menu import Menu

class Bet:
    def __init__(self, player_token): 
        self.player_token = player_token
        self.table_bet = 0

    def drop_bet(self):
        print("Vous avez", self.player_token,"jetons.")
        if self.player_token < 5:
            print("Vous n'avez plus assez de jeton !!")
            menu = Menu()
            menu.main_title()
        
        while (self.table_bet < 5) or (self.table_bet > self.player_token):
            self.table_bet = int(input("Combien voulez vous parier ?"))
            if self.table_bet < 5:
                print("Vous devez parier au moins 5 jetons...")
            elif self.table_bet > self.player_token:
                print("Vous n'avez pas cette quantité de jeton...")

        self.player_token -= self.table_bet
        print("Les jeux sont fait !!")
    
    def results_final(self):
        if self.is_blackjack == True :
            self.tockens_player += self.table_bet * 2.5
            print("Votre mise est 2.5 fois augmentée")

        elif self.islost == True:
            print("vous perdez")

        else:
            print("vous gagnez!")
            self.tockens_player = self.score * 2
            print("votre mise mise est 2 fois augmentée")
