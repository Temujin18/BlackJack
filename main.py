import deck
import dealer
import player as p

deck_of_cards = deck.CardDeck()

dealer = dealer.Dealer(deck_of_cards)


def check_dealer_against_player(dealer, player):
    if dealer.evaluate_hand_blackjack(player.hand) > dealer.evaluate_hand_blackjack(dealer.hand):
        print('Player wins!')
    elif dealer.evaluate_hand_blackjack(dealer.hand) == dealer.evaluate_hand_blackjack(player.hand):
        print('Push! Neither wins!')
    else:
        print('Dealer wins!')


def main():
    print('Welcome to CLI BlackJack! Single Deck, 1 Player')
    name = input('What is your name?\n')

    player = p.Player(name)

    print('Dealing initial hand of cards to {} and dealer...'.format(player.name))
    player.add_to_hand(dealer.draw_card(), dealer.draw_card())
    dealer.add_to_hand(dealer.draw_card(), dealer.draw_card())

    print('Player hand is: {} Value: {}'.format(player.show_hand(), dealer.evaluate_hand_blackjack(player.hand)))
    print('Showing one of two dealer hand: {}'.format(dealer.show_initial_hand()))

    while dealer.evaluate_hand_blackjack(player.hand) < 21:
        is_player_hit = input('Does the player want to hit? or stand? [Please type h or s]\n')

        while is_player_hit not in ['h', 's']:
            is_player_hit = input('Please type h for hit or s for stand\n')

        if is_player_hit == 'h':
            player.add_to_hand(dealer.draw_card())
            print('Player hand is now {} Value: {}'.format(player.show_hand, dealer.evaluate_hand_blackjack(player.hand)))
        else:
            print('Player has chosen to stand.')
            print('Dealer hand is {} Value: {}'.format(dealer.show_hand(),
                                                       dealer.evaluate_hand_blackjack(dealer.hand)))
            while dealer.evaluate_hand_blackjack(dealer.hand) <= 16:
                print('Dealer hand is less than 17, drawing another card for dealer.')
                dealer.add_to_hand(dealer.draw_card())
                print('Dealer hand is {} Value: {}'.format(dealer.show_hand(),
                                                           dealer.evaluate_hand_blackjack(dealer.hand)))
            if dealer.evaluate_hand_blackjack(dealer.hand) > 21:
                print('Dealer is bust!')
                print('Player wins!')
                break

            check_dealer_against_player(dealer, player)
            break

    if dealer.evaluate_hand_blackjack(player.hand) > 21:
        print('Player is bust!')
    elif dealer.evaluate_hand_blackjack(player.hand) == 21:
        print('BlackJack! Player wins!')


if __name__ == '__main__':
    main()
