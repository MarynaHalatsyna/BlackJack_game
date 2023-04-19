import random


# when ace is in hand, check if it should be 11 or 1
def calc_score(player):
    hand = []
    for i in player:
        hand.append(int(cards_lib[i]))

        # change 1 - included this to for loop
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
    score = sum(hand)
    return score


# to define function -> when card is selected, it is removed from the list
def select_card(player):
    new_card = random.choice(cards)
    player.append(new_card)
    cards.remove(new_card)


# to define user turn function
def user_turn():
    # to add one card and calculate score
    select_card(user)

    # to check if sum is more than 21 and there is an ace -> replace it with 1 and calculate score once again
    user_sc = calc_score(user)

    # if there is no exceeding of 21 -> ask if user want to continue
    if user_sc < 21:
        print(f"\nYou cards are {user}, current score is {user_sc}.")
        quest = input("Do you want to open another card? y / n: ")

        # if answer is yes -> repeat from the beginning
        if quest == "y":
            user_turn()

        # if answer is no -> print final result
        else:
            print(f"\nYour final hand is {user}, final score is {user_sc}.")

    # if score is already more than 20 -> stop the function and print results
    else:
        print(f"\nYour final hand is {user}, final score is {user_sc}.")


# define computer's turn
def comp_turn():
    # to add one card and calculate score
    select_card(comp)

    # to check if sum is more than 21 and there is an ace -> replace it with 1 and calculate score once again
    comp_sc = calc_score(comp)

    # if score is less than 17, computer should select one more card
    if comp_sc < 17:
        print(f"\nComputer's cards are {comp}, current score is {comp_sc}.")
        print("Computer selects next card.")
        comp_turn()

    # if score is 17 and more, computer finishes its turn
    else:
        print(f"\nComputer's final hand is {comp}, final score is {comp_sc}.")


# to define final wording
def final_wording(final_score_comp, final_score_user):
    if final_score_user < final_score_comp:
        return "\nYou are a bankrupt!"
    elif final_score_user > final_score_comp:
        return "\nYou are a billionaire!"
    else:
        return "\nYou just lost your time."


# parameter to decide if the game should be continued
cont = True

# amount of win / lost
counter_comp = 0
counter_user = 0

# library for cards
cards_lib = {"♣Ace": 11, "♣2": 2, "♣3": 3, "♣4": 4, "♣5": 5, "♣6": 6, "♣7": 7, "♣8": 8, "♣9": 9, "♣10": 10, "♣King": 10,
             "♣Queen": 10, "♣Jack": 10,
             "♦Ace": 11, "♦2": 2, "♦3": 3, "♦4": 4, "♦5": 5, "♦6": 6, "♦7": 7, "♦8": 8, "♦9": 9, "♦10": 10, "♦King": 10,
             "♦Queen": 10, "♦Jack": 10,
             "♥Ace": 11, "♥2": 2, "♥3": 3, "♥4": 4, "♥5": 5, "♥6": 6, "♥7": 7, "♥8": 8, "♥9": 9, "♥10": 10, "♥King": 10,
             "♥Queen": 10, "♥Jack": 10,
             "♠Ace": 11, "♠2": 2, "♠3": 3, "♠4": 4, "♠5": 5, "♠6": 6, "♠7": 7, "♠8": 8, "♠9": 9, "♠10": 10, "♠King": 10,
             "♠Queen": 10, "♠Jack": 10, }

while cont is True:

    # to create empty lists
    comp = []
    user = []

    # to create list of cards based on library
    cards = []
    for key in cards_lib:
        cards.append(key)

    # first turn by the computer
    select_card(comp)
    comp_sc = calc_score(comp)
    print("\n------------------------------------\nLets start!\n")
    print(f"Computer's first card is {comp}, current score is {comp_sc}.")

    # first turn of the user
    select_card(user)

    # next turns of user -> till user decides to not continue or score is more than 20
    # (there is a Black Jack or overrun)

    user_turn()
    user_sc = calc_score(user)

    # check if there is a Black Jack or run-over (in this case computer's turn is not needed)

    # Black Jack check
    if len(user) == 2 and user_sc == 21:
        print("\nBlack Jack, you won!")
        counter_user += 1

    # overrun check
    elif user_sc > 21:
        print("\nYou went over, computer won.")
        counter_comp += 1

    # all other situations
    else:

        # comp_turn -> till computer score is 17 or more
        comp_turn()
        comp_sc = calc_score(comp)

        # check of winner

        # Black Jack check for computer
        if len(comp) == 2 and comp_sc == 21:
            print("\nBlack Jack, computer won!")
            counter_comp += 1

        # overrun check for computer
        elif comp_sc > 21:
            print("\nComputer went over, you won!")
            counter_user += 1

        # Draw check
        elif comp_sc == user_sc:
            print("\nDraw.")

        # Score comparison checks
        elif comp_sc > user_sc:
            print("\nYou lose!")
            counter_comp += 1
        elif comp_sc < user_sc:
            print("\nYou win!")
            counter_user += 1

    # Question if the user wants to play one more game -> if yes it will be repeated from the beginning
    quest_cont = input("\nDo you want to play once again? y / n: ")

    # if user wants to finish _> parameter is changed, so the loop will be not repeated
    if quest_cont == "n":
        cont = False
        final_words = final_wording(counter_comp, counter_user)

        # final words
        print(f"\nThank you for the game, game result is {counter_user}:{counter_comp}.\n {final_words} See you later!")
