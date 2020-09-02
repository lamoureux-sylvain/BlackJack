from user import User


class Table:
    def __init__(self, nb_players):
        self.table_capacity = ["1", "2", "3", "4"]
        self.nb_players = nb_players

    def get_in(self):
        print("\nBienvenue à la table !\n")
        while self.nb_players not in self.table_capacity:
            self.nb_players = input("Combien êtes-vous ? ")
        self.nb_players = int(self.nb_players)
        return Table(self.nb_players)

    def get_out(self):
        pass

    def play(self):
        print("\nLa partie peut commencer !")
