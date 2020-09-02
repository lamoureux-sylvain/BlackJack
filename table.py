from user import User

class Table:
    def __init__(self, nb_players):
        self.table_capacity = ["1","2","3","4"]
        self.nb_players = nb_players
        self.character = "abcdefghijklmnopqrstuvwxyzéèàù+=/:;.,?@#'(§!ç-_$*%"

    def get_in(self):
        print("\nBienvenue à la table !\n")
        while self.nb_players not in self.table_capacity:   
            self.nb_players = input("Combien êtes-vous ? ").lower()
            if self.nb_players in self.character:
                print("Veuillez entrer un chiffre...")
            elif self.nb_players not in self.table_capacity:
                print("La table peut acceuillir entre 1 et 4 joueurs")
        self.nb_players = int(self.nb_players)
        return Table(self.nb_players)

    def get_out(self):
        pass

    def play(self):
        print("\nLa partie peut commencer !")
