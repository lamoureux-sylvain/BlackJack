from deck import Deck
from hand import Hand
from bet import Bet
from user import User
from menu import Menu


class Game:
    def __init__(self):
        # Initialisation des joueurs
        self.user = User([])
        # Appel de la méthode pour créer les joueurs
        self.user.generate_player()
        # Appel du nom des joueurs
        self.players = self.user.players
        # Initialisation des paris
        self.bet = Bet(1000)
        # Initialisation du paquet
        self.deck = Deck()
        # Appel de la méthode pour mélanger le paquet
        self.deck.shuffle()

    def play(self):
        # Initialisation de l'état de la partie
        playing = True

        # Initialisation du nombre de tour
        self.tour = 1

        # Partie
        while playing:
            # Affichage du nombre de tour
            print(
                r"""+===================================================================+ """
            )
            print(
                "|                              TOUR",
                self.tour,
                ":                             |",
            )
            print(
                r"""+===================================================================+ """
            )
            # Compteur de tour
            self.tour += 1

            # Appel de la méthode pour parier
            self.bet.drop_bet()
            # Appel des jetons du joueur après pari
            self.player_token = self.bet.player_token
            # Initialisation des mains des joueurs
            self.player_hand = Hand()
            # Initialisation de la main du dealer
            self.dealer_hand = Hand(dealer=True)

            # 1e carte
            self.nb_card = 1
            # Le croupier distribue une 1e carte aux joueurs
            self.player_hand.add_card(self.deck.deal())
            # Le croupier se distribue une 1e carte
            self.dealer_hand.add_card(self.deck.deal())

            # 2e carte
            self.nb_card = 2
            # Le croupier distribue une 1e carte aux joueurs
            self.player_hand.add_card(self.deck.deal())
            # Affichage de la main du joueur

            print(
                r"""+-------------------------------------------------------------------+"""
            )
            print()
            print("Votre main:\n")
            self.player_hand.display(self.nb_card)
            print()
            print(
                r"""+-------------------------------------------------------------------+"""
            )
            # Le croupier se distribue une 1e carte
            self.dealer_hand.add_card(self.deck.deal())
            # Affichage de la main du croupier
            print(
                r"""+-------------------------------------------------------------------+"""
            )
            print()
            print("Main de la Banque:\n")

            self.dealer_hand.display(self.nb_card)
            print()
            print(
                r"""+-------------------------------------------------------------------+"""
            )

            # n carte suivante
            self.nb_card = 3

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack:
                    dealer_has_blackjack = False
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack
                    )
                    continue
                print(
                    r"""+===================================================================+ """
                )

                choice = input(
                    "\n            Que voulez vous faire ? [Piocher / Sauver] "
                ).lower()
                print()
                while choice not in ["p", "s", "piocher", "sauver"]:
                    choice = input(
                        "            Entrer 'piocher' ou 'sauver' (ou P/S) "
                    ).lower()
                if choice in ["piocher", "p"]:
                    print("Votre main:\n")
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display(self.nb_card)
                    if self.player_is_over():
                        print(
                            r"""+===================================================================+ """
                        )
                        print("\n                          C'est perdu !")
                        print(
                            "\n                    Vous perdez",
                            self.bet.table_bet,
                            "jetons...",
                        )
                        print()
                        print(
                            r"""+===================================================================+ """
                        )
                        game_over = True
                        Bet(self.player_token)
                else:
                    if dealer_has_blackjack:
                        player_has_blackjack = False
                        game_over = True
                        self.show_blackjack_results(
                            player_has_blackjack, dealer_has_blackjack
                        )
                        continue
                    else:
                        player_hand_value = self.player_hand.get_value()
                        print()

                        print(
                            r"""+-------------------------------------------------------------------+"""
                        )
                        print("\nMain de la Banque:\n")
                        self.dealer_hand.display(self.nb_card)
                        dealer_hand_value = self.dealer_hand.get_value()
                        print()

                    if dealer_hand_value < 17:
                        while dealer_hand_value < 17:
                            self.dealer_hand.add_card(self.deck.deal())
                            dealer_hand_value = self.dealer_hand.get_value()
                            print()
                            print(
                                r"""+-------------------------------------------------------------------+"""
                            )
                            print("\nLe croupier doit retirer une carte\n")
                            print("Main de la Banque:")
                            self.dealer_hand.display(self.nb_card)
                            print()
                            print(
                                r"""+-------------------------------------------------------------------+"""
                            )

                    print("\n                       Score final\n")
                    print("Votre main:", player_hand_value)
                    print()
                    print("Main de la banque:", dealer_hand_value)
                    print()

                    if player_hand_value > dealer_hand_value:
                        print("C'est gagné!\n")
                        self.bet.win_gain()
                    elif player_hand_value == dealer_hand_value:
                        print("Égalité... La Banque gagne!\n")
                        print("Vous perdez", self.bet.table_bet, "jetons...")
                        Bet(self.player_token)
                    elif dealer_hand_value > 21:
                        print("C'est gagné!\n")
                        self.bet.win_gain()
                    else:
                        print("La Banque gagne!\n")
                        print("Vous perdez", self.bet.table_bet, "jetons...")
                        Bet(self.player_token)
                    game_over = True

            again = input("\nContinuer? [O/N] \n")
            while again.lower() not in ["o", "n"]:
                again = input("Entrer O ou N ")
            if again.lower() == "n":
                print("\nMerci d'avoir joué!\n")
                playing = False
            else:
                game_over = False

        menu = Menu()
        menu.main_title()

    def player_is_over(self):
        return self.player_hand.get_value() > 21

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack:
            print(
                r"""+===================================================================+ """
            )
            print(
                "|               Blackjack !!!!!! Bravo",
                self.players[0],
                "!!!!!!               |",
            )
            print(
                r"""+===================================================================+ """
            )

            self.bet.black_jack_gain()
        elif dealer_has_blackjack:
            print(
                r"""+===================================================================+ """
            )
            print(
                "|                   Blackjack pour la Banque!                       |"
            )
            print(
                r"""+===================================================================+ """
            )


if __name__ == "__main__":
    game = Game()
    game.play()