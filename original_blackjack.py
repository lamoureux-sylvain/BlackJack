import random
class Bet:
    def __init__(self, tokens): #tokken init 1000
        
        self.tockens_player = tokens
        self.table_bet = 0

    def drop_bet(self):
        print("Vous avez", self.tockens_player,"jetons.")
        while self.table_bet < 1 or self.table_bet > self.tockens_player:
            self.table_bet = int(input("Combien voulez vous parier ?"))
        self.tockens_player -= self.table_bet
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
            


if __name__ == "__main__":
    bet = Bet(1000)     
    bet.drop_bet()   
            
            
  




