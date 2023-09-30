import random

print(
    """ _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 """
)
cards_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
player_cards = []
dealer_cards = []


def card_score(card):
    if card == "A":
        return 11
    return (cards_list.index(card) + 1) if (cards_list.index(card) + 1) < 11 else 10


def add_player_card():
    player_cards.append(random.choice(cards_list))


def add_dealer_card():
    dealer_cards.append(random.choice(cards_list))


start = input("Would you like to play a game of Blackjack? (y/n)")
if start == "y":
    player_score = 0
    dealer_score = 0
    add_player_card()
    add_player_card()
    for i in player_cards:
        player_score += card_score(i)
    print(f"Your cards:[{', '.join(player_cards)}]")

    # Winning condition one card is an Ace and the other card is valued at 10 or face-card
    if (player_cards[0] == "A" and cards_list.index(player_cards[1]) > 9) or (
        player_cards[0] == "A" and cards_list.index(player_cards[1]) > 9
    ):
        print("****BlackJack**** You Win!!")
    # otherwise the player must have cards less than value of 21
    # user can take a card ==> win (21), bust (>21), no-bust (<21) - user can select to hit or stand [ loop condition ]
    else:
        print(f"Player score is {player_score}")
        add_dealer_card()
        add_dealer_card()
        print(f"Dealer open card: [{dealer_cards[0]}]")
        # print(f"Dealer hidden card: [{dealer_cards[1]}]")
        if (dealer_cards[0] == "A" and cards_list.index(dealer_cards[1]) > 9) or (
            dealer_cards[0] == "A" and cards_list.index(dealer_cards[1]) > 9
        ):
            print("****BlackJack**** Dealer Wins!!")
        for i in dealer_cards:
            dealer_score += card_score(i)

        while True:
            card_choice = input("Hit or stand?: (hit/stand) ")
            if card_choice == "stand":
                break
            add_player_card()
            player_score += card_score(player_cards[len(player_cards) - 1])
            print(f"Your cards:[{', '.join(player_cards)}]")
            print(f"Player score is {player_score}")
            if player_score == 21:
                print("You win!")
                exit()
            if player_score > 21:
                if player_cards[0] == "A" or player_cards[1] == "A":
                    print(f"Adjusting value of Ace to 1")
                    player_score -= 10
                    print(f"Player score is {player_score}")
                # sys.exit("Bust!") runs as exception on interpreter, doesn't have wanted effect when run in VScode
                else:
                    print("Bust!")
                    exit()  # exits program closes more efficiently, no output statement

        # check the dealer score
        print(f"Dealer cards:[{', '.join(dealer_cards)}]")
        print(f"Dealer score: {dealer_score}")
        while True:
            if dealer_score < 18:
                # hit for dealer
                add_dealer_card()
                dealer_score += card_score(dealer_cards[len(dealer_cards) - 1])
                print(f"Dealer cards:[{', '.join(dealer_cards)}]")
                print(f"Dealer score: {dealer_score}")
                if dealer_score == 21:
                    print("Dealer wins!")
                    exit()
                if dealer_score > 21:
                    print("Dealer busts! You win")
                    exit()
            else:
                print("Dealer stands")
                print(f"Your cards:[{', '.join(player_cards)}]")
                print(f"Dealer cards:[{', '.join(dealer_cards)}]")
                print(f"Your score: {player_score}")
                print(f"Dealer score: {dealer_score}")
                if player_score > dealer_score:
                    print("You win!")
                else:
                    print("Dealer wins!")
                break

else:
    print("Okay thanks for playing")
