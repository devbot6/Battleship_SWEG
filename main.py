import random

class ships:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col


#input verificiation 
some_bool = True
while (some_bool):
    print('            ')
    #user input to set gridSize
    gridSize = input("How big do you want it to be?(5 = 5x5)(Must be greater than 2)")
    print("        ")
    #user input to set the mode whether the ships are selected or random
    userChoice = input("Do you want it to be Selected or Random? (1=Selected, 2=Random)")
    
    try:
        #evaluates the value of userRow and userCol
        gridSize = eval(gridSize)
        userChoice = eval(userChoice)
    except:
        #will run this if it errors
        print("         ")
        print("That not a valid input try again!")
        some_bool = True
    if str != type(gridSize) and str != type(userChoice) and (userChoice <3) and (userChoice > 0) and (gridSize>2):   
        some_bool = False
    else:
        print("   ")
        print("That not a valid input try again!")


#creates board
guessBoard = [["0"] * gridSize for i in range(gridSize)]
compGuessBoard = [["0"] * gridSize for i in range(gridSize)]
#board used to store the computer's ships
computerShips = []
#board used to store the user's ships
userShips = []

#returns the random location in the grid 
if userChoice == 2:
    for i in range(2):
        name = input("Name for ship {}: ".format(i))
        #makes a list for a specific ship
        compShip = []
        #generates 2 random numbers
        randomRow1 = random.randrange(1,gridSize)
        randomCol1 = random.randrange(1,gridSize)
        
        compShip = ships(name, randomRow1, randomCol1)
        
        #append the single ship list to the list of ships
    computerShips.append(compShip)
        
        
elif userChoice == 1:
    for i in range(1):
        #makes a list for a specific ship
        compShip = []
        #while loop for input verification
        some_bool = True
        while (some_bool):
            print("             ")
            #used to set the computer's ship row
            userRow = input("What row would you like for the computer's's ship {} :".format(i+1))
            print("       ")
            #used to set the computer's ship column
            userCol = input("What column would you like for the computer's ship {} :".format(i+1))
            
            try:
                #evaluates the value of userRow and userCol
                userRow = eval(userRow)
                userCol = eval(userCol)
            except:
                #runs this if it errors
                print("          ")
                print("That not a valid input try again!")
                some_bool = True
            if str != type(userRow) and str != type(userCol) and (userCol <= gridSize) and (userRow <= gridSize):   
                some_bool = False
            else:
                print("   ")
                print("That not a valid input try again!")
            
        name = input("Name for ship {}: ".format(i))
        compShip = (name, userRow, userCol)
        computerShips.append(compShip)
        
                
                   

        

for i in range(1):
        #single ship list
        userShip = []
        #while loop for input verification
        some_bool = True
        while (some_bool):
            print("             ")
            #used to set the user's ship row
            userRow = input("What row would you like for your ship {} :".format(i+1))
            print("       ")
            #used to set the user's ship column
            userCol = input("What column would you like for your ship {} :".format(i+1))
            
            try:
                #evaluates the value of userRow and userCol
                userRow = eval(userRow)
                userCol = eval(userCol)
            except:
                #if the above code erros it runs this
                print("   ")
                print("That not a valid input try again!")
                some_bool = True
            if str != type(userRow) and str != type(userCol) and (userCol <= gridSize) and (userRow <= gridSize):   
                some_bool = False
            else:
                print("   ")
                print("That not a valid input try again!")
            
        name = input("Name for ship {}: ".format(i))
        userShip = (name, userRow, userCol)
        #appends the user ship to the list of userSHips
        userShips.append(userShip)

#function used for the computers side of playing
def computerPlay():
    print("--------------------------------------Computer Turn-----------------------------------------------------")
    #prints board
    print("ENEMY BOARD")
    print('\n'.join(' '.join(map(str,sl)) for sl in compGuessBoard))

    #amount of turns represented as ammo and ship lives
    ammo = 5
    ships_left = 1
    while ammo>0:
            print("COMPUTER'S TURN")
            
            row = random.randint(1, gridSize)
            column = random.randint(1, gridSize)
            
           
            print("-----------------------------------------------------------------------")
            print("The computer guessed row: {} col: {}".format(row, column))


            choice = [row, column]

            #ensures the user cannot type outisde of the bounds of the grid
            if row not in range(1,gridSize+1) or column not in range(1, gridSize+1):
                print("\nThe numbers must be between 1-{}!".format(gridSize))
                ammo-=1
                continue


            row = row - 1 # Reducing number to desired index.
            
            
            #checks to see if you shot a spot already  
            if compGuessBoard[row][column] == "-" or compGuessBoard[row][column] == "X":
                print("\nYou have already shot that spot!\n")
                continue
            #compares the list of computer ships and checks to see if choice list matches any of them
            elif choice in userShips:
                print("\nBoom! You hit! A ship has exploded!\n")
                compGuessBoard[row][column] = "X"
                #if its a hit it loses ammo and a ship dies
                ships_left -= 1
                ammo -= 1
                # if no more ships you win
                if ships_left == 0:
                    print("Congrats, you won! (COMPUTER WON)")
                    break
            else:
                # prints a - if you miss
                print("\nYou missed!\n")
                compGuessBoard[row][column] = "-"
                ammo -= 1
                
            # prints board
            print("ENEMY BOARD")
            for i in compGuessBoard:
                print(*i)
                
        
            print("  ")
            # prints your current ammo and ships lives every turn
            print(f"Ammo left: {ammo} | Ships left: {ships_left}")
            print("  ")


#overarching funtion that runs the core process of the game
def play_game():
    print("-----------------------------------USER TURN-----------------------------------------------")
    #prints board
    print("ENEMY BOARD")
    print('\n'.join(' '.join(map(str,sl)) for sl in guessBoard))

    #amount of turns represented as ammo and ship lives
    ammo = 5
    ships_left = 1
    while ammo>0:

            print("USER'S TURN")
            try:
                #attempts to run this code
                row = int(input("You must enter a row number between 1-{} >: ".format(gridSize)))
                column = int(input("You must enter a column number between 1-{} >: ".format(gridSize)))
                print("---------------------------------------------------------------------------------")
            except ValueError:
                #runs this code if it errors out with a valueError
                print("You wont break my code, number only!")
                continue
            #stores the input into a list
            choice = [row, column]
            
            print("You guessed row: {} col: {}".format(row, column))
            
            #ensures the user cannot type outisde of the bounds of the grid
            if row not in range(1,gridSize+1) or column not in range(1, gridSize+1):
                print("\nThe numbers must be between 1-{}!".format(gridSize))
                ammo-=1
                continue


            row = row - 1 # Reducing number to desired index.
            column = column - 1 # Reducing number to desired index.
            
            
            #checks to see if you shot a spot already  
            if guessBoard[row][column] == "-" or guessBoard[row][column] == "X":
                print("\nYou have already shot that spot!\n")
                continue
            #compares the list of computer ships and checks to see if choice list matches any of them
            elif
                for ships in computerShips:
                    if compShip.row == choice[0] and compShip.col == choice[1]:
                        print("\nBoom! You hit!\n")
                        guessBoard[row][column] = "X"
                        #if its a hit it loses ammo and a ship dies
                        ships_left -= 1
                        ammo -= 1
                        # if no more ships you win
                        if ships_left == 0:
                            print("Congrats, you won! (USER WON)")
                            computerPlay()
                            break
               
            else:
                # prints a - if you miss
                print("\nYou missed!\n")
                guessBoard[row][column] = "-"
                ammo -= 1
            # prints board
            print("ENEMY BOARD")
            for i in guessBoard:
                print(*i)
            
            print("  ")
            # prints your current ammo and ships lives every turn
            print(f"Ammo left: {ammo} | Ships left: {ships_left}")
            print("   ")
            
            if ammo == 0:
                computerPlay()

# runs core fucntion
play_game()




