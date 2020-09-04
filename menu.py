class Menu:
    def __init__(self):
        pass

    def main_title(self):
        self.player_choice = ""
        self.choices = ["n", "r", "c", "q"]
        print(
            r"""+===================================================================+ """
        )
        print(
            r"""|                                                                   | 
|                           _ _.-'`-._ _                            |
|                          ;.'________'.;                           |
|               _________n.[____________].n_________                |
|              |""_""_""_""||==||==||==||""_""_""_""]               |
|              |'''''''''''||==||==||==||'''''''''''|               |
|              |LI LI LI LI||LI||LI||LI||LI LI LI LI|               |
|              |.. .. .. ..||..||..||..||.. .. .. ..|               |
|              |LI LI LI LI||LI||LI||LI||LI LI LI LI|               |
|                                                                   |
|     ,adPPYba, ,adPPYYba, ,adPPYba, 88 8b,dPPYba,   ,adPPYba,      |
|    a8"     "" ""     `Y8 I8[    "" 88 88P'   `"8a a8"     "8a     |
|    8b         ,adPPPPP88  `"Y8ba,  88 88       88 8b       d8     |
|    "8a,   ,aa 88,    ,88 aa    ]8I 88 88       88 "8a,   ,a8"     |
|     `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"' 88 88       88  `"YbbdP"'      |
|                                                                   |"""
        )
        print(
            r"""+-------------------------------------------------------------------+"""
        )
        print(
            r"""|                                                                   | 
|             ____  _            _     _            _               |
|            | __ )| | __ _  ___| | __(_) __ _  ___| | __           |
|            |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /           |
|            | |_) | | (_| | (__|   < | | (_| | (__|   <            |
|            |____/|_|\__,_|\___|_|\_\/ |\__,_|\___|_|\_\           |
|                                    |__/                           |"""
        )
        print(
            r"""+-------------------------------------------------------------------+"""
        )
        print(
            """|              Bienvenue à votre table de BLACK JACK!!              |"""
        )
        print(
            r"""+===================================================================+     
|                   ___________       ___________                   |
|                  /           \     /           \                  |
|                  | A       A |     | J       J |                  |
|                  | #       # |     | #       # |                  |
|                  |           |     |           |                  |
|                  |     #     |     |     #     |                  |
|                  |           |     |           |                  |
|                  | #       # |     | #       # |                  |
|                  |  A      A |     | J       J |                  |
|                  \___________/     \___________/                  |
|                                                                   |"""
        )
        print("---------------------------------------------------------------------\n")
        print(
            r"""+===================================================================+ """
        )
        print(
            r"""|                          - Nouvelle partie (N)                    |"""
        )
        print(
            r"""|                          - Règles (R)                             |"""
        )
        print(
            r"""|                          - Classement (C)                         |"""
        )
        print(
            r"""|                          - Quitter (Q)                            |"""
        )
        print(
            r"""+===================================================================+ """
        )
        while self.player_choice not in self.choices:
            print(
                r"""|              Bienvenue ! Que souhaitez vous faire ?               |"""
            )
            print(
                r"""+===================================================================+ """
            )
            self.player_choice = input().lower()

        if self.player_choice == "n":
            Menu().new_game()
        elif self.player_choice == "r":
            Menu().rules()
        elif self.player_choice == "c":
            Menu().leaderboard()
        else:
            Menu().quit()

    def new_game(self):
        print(
            r"""+===================================================================+ """
        )
        print(
            """|                          NOUVELLE PARTIE !!                       |"""
        )
        print("---------------------------------------------------------------------\n")

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
