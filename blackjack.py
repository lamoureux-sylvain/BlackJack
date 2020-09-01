class Blackjack:
    def __init__(self):
        pass
    
    def menu(self):
        self.player_choice = ""
        self.choices = ["n","r","c","q"]
        print("""                          BLACK JACK!!""")
        print("""------------------------------------------------------------------\n""")
        print("- Nouvelle partie (N)\n- Règles (R)\n- Classement (C)\n- Quitter (Q)\n")
        while self.player_choice not in self.choices:
            self.player_choice = input("Bienvenue ! Que souhaitez vous faire ? ").lower()

        if self.player_choice == "n":
            Blackjack().new_game()
        elif self.player_choice == "r":
            Blackjack().rules()
        elif self.player_choice == "c":
            Blackjack().leaderboard()
        else:
            Blackjack().quit()

    def new_game(self):
        print("\nNouvelle Partie !")
    
    def rules(self):
        self.player_choice = ""
        print("""\n                                       Les règles du Black Jack !!\n""")
        print("Va voir sur Google ce sera plus simple !\n")
        while self.player_choice != "q":
            self.player_choice = input("Menu principal (Q) : ").lower()
        if self.player_choice == "q":
            Blackjack().menu()
    
    def leaderboard(self):
        self.player_choice = ""
        print("""\n                                   Classement...""")
        print("""1. Éléonore D'Herbigny
2. Cyril Simonin
3. Syvain Lamoureux
3. Alexandre Vilbert
3. Étienne Rist
4. Rolique Oponga\n""")
        while self.player_choice != "q":
            self.player_choice = input("Menu principal (Q) : ").lower()
        if self.player_choice == "q":
            Blackjack().menu()

    def quit(self):
        exit()

if __name__ == "__main__":
    Blackjack().menu()


