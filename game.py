from deck import Deck
from hand import Hand
from bet import Bet
from user import User


class Game:
    def __init__(self):
        pass

    def play(self):
        playing = True

        user = User([])
        user.generate_player()
        self.player_token = user.player_token

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.bet = Bet(self.player_token)
            self.bet.drop_bet() 

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Votre main:")
            self.player_hand.display()
            print()
            print("Main de la Banque:")
            self.dealer_hand.display()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack
                    )
                    continue

                choice = input("Que voulez vous faire ? [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Entrer 'hit' ou 'stick' (ou H/S) ").lower()
                if choice in ["hit", "h"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("C'est perdu !")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    if dealer_hand_value < 17:
                        while dealer_hand_value < 17:
                            self.dealer_hand.add_card(self.deck.deal())
                            dealer_hand_value = self.dealer_hand.get_value()
                            print("Le croupier doit retirer une carte")
                            print("Main de la Banque:")
                            self.dealer_hand.display()

                    print("Score final")
                    print("Votre main:", player_hand_value)
                    print("Main de la banque:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("C'est gagné!")
                    elif player_hand_value == dealer_hand_value:
                        print("La Banque gagne!")
                    elif dealer_hand_value > 21:
                        print("C'est gagné!")
                    else:
                        print("La Banque gagne!")
                    game_over = True

            again = input("Continuer? [O/N] ")
            while again.lower() not in ["o", "n"]:
                again = input("Entrer O ou N ")
            if again.lower() == "n":
                print("Merci d'avoir joué!")
                playing = False
            else:
                game_over = False

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
        if player_has_blackjack and dealer_has_blackjack:
            print("Blackjack pour le joueur et la Banque! Draw!")

        elif player_has_blackjack:
            print("Blackjack !!!!!! C'est gagné !!!!!!")

        elif dealer_has_blackjack:
            print("Blackjack pour la Banque!")


if __name__ == "__main__":
    game = Game()
    game.play()