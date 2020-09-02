from menu import Menu
from table import Table
from user import User

if __name__ == "__main__":
    table = Table(0)
    menu = Menu()
    menu.main_title()
    table.get_in()
    user = User(table.nb_players)
    user.generate_player()
