from menu import Menu
from table import Table
from user import User
from game import Game


if __name__ == "__main__":
    menu = Menu()
    menu.main_title()

    game = Game()
    game.play()
