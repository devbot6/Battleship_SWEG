import random


gridSize = eval(input("How big do you want it to be?(5 = 5x5)"))

userChoice = input("""Do you want it to be "Selected" or "Random"?""")

#creates board
guessBoard = [["0"] * gridSize for i in range(gridSize)]
ships = []

#prints board
def printBoard():
    print(guessBoard)
    

#returns the random location in the grid 
if userChoice == "Random":
    for i in range(3):
        ship = []
        
        randomRow1 = random.randrange(1,gridSize)
        randomCol1 = random.randrange(1,gridSize)
        
        ship.append(randomRow1)
        ship.append(randomCol1)
        
        ships.append(ship)
        
elif userChoice == "Selected":
    for i in range(3):
        ship = []
        
        userRow = eval(input("What row would you like for this ship:"))
        userCol = eval(input("What column would you like for this ship:"))
        
        ship.append(userRow)
        ship.append(userCol)
        
        ships.append(ship)


def play_game():
    print('\n'.join(' '.join(map(str,sl)) for sl in guessBoard))
    ammo = 5
    while ammo>0:
            try:
                row = int(input("You must enter a row number between 1-{} >: ".format(gridSize)))
                column = int(input(" You must enter a column number between 1-{} >: ".format(gridSize)))
            except ValueError:
                print("You wont break my code, number only!")
                continue
            
            choice = [row, column]
            
            
            if row not in range(1,gridSize+1) or column not in range(1, gridSize+1):
                print("\nThe numbers must be between 1-{}!".format(gridSize))
                ammo-=1
                continue

            row = row - 1 # Reducing number to desired index.
            column = column - 1 # Reducing number to desired index.
            
            
            ships_left = 3
            
            if guessBoard[row][column] == "-" or guessBoard[row][column] == "X":
                print("\nYou have already shot that spot!\n")
                continue
            elif choice in ships:
                print("\nBoom! You hit! A ship has exploded! You were granted a new ammo!\n")
                guessBoard[row][column] = "X"
                ships_left -= 1
                if ships_left == 0:
                    print("Congrats, you won!")
            else:
                print("\nYou missed!\n")
                guessBoard[row][column] = "-"
                ammo -= 1

            for i in guessBoard:
                print(*i)

            print(f"Ammo left: {ammo} | Ships left: {ships_left}")


play_game()




