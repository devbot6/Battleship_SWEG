print ("Welcome to the game of Battleship")

import random
def create_random_ship():
    return random.randint(0, 5), random.randint(0, 5)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ships_left = 3


def play_agian():
    try_again = input("Wanna play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
        