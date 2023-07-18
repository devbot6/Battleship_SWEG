import random


some_bool = True
while (some_bool):
    print("         ")
    gridSize = input("How big do you want it to be?(5 = 5x5)")
    print("            ")
    userChoice = input("Do you want it to be Selected or Random? (1=Selected, 2=Random)")
    print("              ")
    shipNum = eval(input("How many ships do you want:"))
    
    try:
        gridSize = eval(gridSize)
        userChoice = eval(userChoice)
        shipNum = eval(shipNum)
    except:
        print("              ")
        print("That is a not a correct input try again")
        some_bool = True
    if str != type(gridSize) and str != type(userChoice) and (userChoice == 1 or 2) and str != type(shipNum):   
        some_bool = False


#creates board
guessBoard = [["0"] * gridSize for i in range(gridSize)]
computerShips = []
userShips = []

#prints board
def printBoard():
    print(guessBoard)
    

#returns the random location in the grid 
if userChoice == 2:
    for i in range(1):
        compShip = []
        
        randomRow1 = random.randrange(1,gridSize)
        randomCol1 = random.randrange(1,gridSize)
        
        compShip.append(randomRow1)
        compShip.append(randomCol1)
        
        computerShips.append(compShip)
        
elif userChoice == 1:
    for i in range(1):
        compShip = []
        
        some_bool = True
        while (some_bool):
            print("             ")
            userRow = input("What row would you like for the comupyer's ship {} :".format(i+1))
            print("       ")
            userCol = input("What column would you like for the computer's ship {} :".format(i+1))
            
            try:
                userRow = eval(userRow)
                userCol = eval(userCol)
            except:
                print("          ")
                print("That is a not a correct input try again")
                some_bool = True
            if str != type(userRow) and str != type(userCol) and (userCol <= gridSize):   
                some_bool = False

        
        compShip.append(userRow)
        compShip.append(userCol)
        
        computerShips.append(compShip)

for i in range(1):
        userShip = []
        
        some_bool = True
        while (some_bool):
            print("             ")
            userRow = input("What row would you like for your ship {} :".format(i+1))
            print("       ")
            userCol = input("What column would you like for your ship {} :".format(i+1))
            
            try:
                userRow = eval(userRow)
                userCol = eval(userCol)
            except:
                print("          ")
                print("That is a not a correct input try again")
                some_bool = True
            if str != type(userRow) and str != type(userCol) and (userCol <= gridSize):   
                some_bool = False


def play_game():
    ammo = eval(input("How many attempts do you want to give yourself: "))  
    #prints the list of lists in a grid format
    print('\n'.join(' '.join(map(str,sl)) for sl in guessBoard))
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
            elif choice in computerShips:
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




