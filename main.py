import random

#creates board
guessBoard = [["0"] * 5 for i in range(5)]


#prints board
def printBoard():
    print(guessBoard)


#returns the random location in the grid 
def randomShips():
    global location1, location2, location3
    
    randomRow1 = random.randrange(1,5)
    randomCol1 = random.randrange(1,5)
    
    location1 = guessBoard[randomRow1][randomCol1]

    randomRow2 = random.randrange(1,5)
    randomCol2 = random.randrange(1,5)
    
    location2 = guessBoard[randomRow2][randomCol2]

    randomRow3 = random.randrange(1,5)
    randomCol3 = random.randrange(1,5)
    
    location3 = guessBoard[randomRow3][randomCol3]
    
    
    
    return randomCol1, randomCol1, randomRow2, randomCol2, randomRow3, randomCol3

def play_again():
    try_again = input("Wanna play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()


def play_game():
    ammo = 3    
    while ammo>0:
            try:
                row = int(input("You must enetr a row number between 1-5 >: "))
                column = int(input(" You must enter a column number between 1-5 >: "))
            except ValueError:
                print("You wont break my code, number only!")
                continue
            
            row1, col1, row2, col2, row3, col3= randomShips()
            
            
            
            if row not in range(1,6) or column not in range(1, 6):
                print("\nThe numbers must be between 1-5!")
                continue

            row = row - 1 # Reducing number to desired index.
            
            
            ships_left = 3
            
            if guessBoard[row][column] == "-" or guessBoard[row][column] == "X":
                print("\nYou have already shot that spot!\n")
                continue
            elif (row, column) == (row1, col2) or (row, column) == (row2, col2) or (row, column) == (row3, col3):
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

            for i in guessBoard:
                print(*i)

            print(f"Ammo left: {ammo} | Ships left: {ships_left}")

#prints the list of lists in a grid format
print('\n'.join(' '.join(map(str,sl)) for sl in guessBoard))

play_game()




