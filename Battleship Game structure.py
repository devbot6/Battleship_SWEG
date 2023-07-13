print ("Welcome to the game of Battleship")

import random


guessBoard = [["x"] * 5 for i in range(5)]



def printBoard():
    print(guessBoard)

def randomShips():
    randomRow = random.randrange(1,5)
    randomCol = random.randrange(1,5)
    
    location = guessBoard[randomRow][randomCol]
    
    return location

def shipHit():
    pass

def shipMissed():
    pass

def shipSunk():
    pass


randomShips()

print('\n'.join(' '.join(map(str,sl)) for sl in guessBoard))


ammo = True



        
while ammo:
        try:
            row = int(input("You must enetr a row number between 1-5 >: "))
            column = int(input(" You must enter a column number between 1-5 >: "))
        except ValueError:
            print("You wont break my code, number only!")
            continue

        if row not in range(1,6) or column not in range(1, 6):
            print("\nThe numbers must be between 1-5!")
            continue

        row = row - 1 # Reducing number to desired index.
        column = column - 1 # Reducing number to desired index.

        if guessBoard[row][column] == "-" or guessBoard[row][column] == "X":
            print("\nYou have already shot that spot!\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("\nBoom! You hit! A ship has exploded! You were granted a new ammo!\n")
           guessBoard[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("Congrats, you won!")
                play_again()
        else:
            print("\nYou missed!\n")
            guessBoard[row][column] = "-"
            ammo -= 1

        for i in game_board:
            print(*i)

        print(f"Ammo left: {ammo} | Ships left: {ships_left}")

def play_agian():
    try_again = input("Wanna play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
        
        