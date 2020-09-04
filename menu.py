class Menu:
    def __init__(self):
        pass

    def main_title(self):
        self.player_choice = ""
        self.choices = ["n", "r", "c", "q"]
        print("""                          BLACK JACK!!""")
        print("------------------------------------------------------------------\n")
        print("- Nouvelle partie (N)\n- Règles (R)\n- Classement (C)\n- Quitter (Q)\n")
        while self.player_choice not in self.choices:
            self.player_choice = input(
                "Bienvenue ! Que souhaitez vous faire ? "
            ).lower()

        if self.player_choice == "n":
            Menu().new_game()
        elif self.player_choice == "r":
            Menu().rules()
        elif self.player_choice == "c":
            Menu().leaderboard()
        else:
            Menu().quit()

    def new_game(self):
        print("""\n                     NOUVELLE PARTIE !!""")
        print("------------------------------------------------------------------\n")

    def rules(self):
        self.player_choice = ""
        print("""\n                 Les règles du Black Jack !!""")
        print("------------------------------------------------------------------\n")
        print("Va voir sur Google ce sera plus simple !\n")
        while self.player_choice != "m":
            self.player_choice = input("Menu principal (M) : ").lower()
        if self.player_choice == "m":
            Menu().main_title()

    def leaderboard(self):
        self.player_choice = ""
        print("""\n                         CLASSEMENT""")
        print("------------------------------------------------------------------\n")
        print(
            """                    1. Éléonore D'Herbigny
                    2. Cyril Simonin
                    3. Syvain Lamoureux
                    3. Alexandre Vilbert
                    3. Étienne Rist
                    3. Rolique Oponga\n"""
        )
        while self.player_choice != "m":
            self.player_choice = input("Menu principal (M) : ").lower()
        if self.player_choice == "m":
            Menu().main_title()

    def quit(self):
        exit()
