import random

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

def userChoices():
    #returns the random location in the grid 
    if userChoice == 2:
        for i in range(1):
            global compName
            #generates 2 random numbers
            randomRow1 = random.randrange(1,gridSize)
            randomCol1 = random.randrange(1,gridSize)
            compName = input("What is the name of the computer ship {}?: ".format(i+1))
            print(randomRow1)
            print(randomCol1)
            #append the single ship list to the list of ships
            guessBoard[randomRow1][randomCol1] = "s"
            
            
    elif userChoice == 1:
        for i in range(1):
            #while loop for input verification
            some_bool = True
            while (some_bool):
                print("             ")
                
                #used to set the computer's ship row
                userRow = input("What row would you like for the computer's's ship {} :".format(i+1))
                print("       ")
                #used to set the computer's ship column
                userCol = input("What column would you like for the computer's ship {} :".format(i+1))
                compName = input("What is the name of the computer ship {}?: ".format(i+1))
                
                try:
                    #evaluates the value of userRow and userCol
                    userRow = eval(userRow)
                    userCol = eval(userCol)
                    compName = eval(compName)
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
                
            guessBoard[userRow][userCol] = "s", compName
            
                    
        
            

    for i in range(1):

            #while loop for input verification
            some_bool = True
            while (some_bool):
                print("             ")
                global userName
                #used to set the user's ship row
                userRow = input("What row would you like for your ship {} :".format(i+1))
                print("       ")
                #used to set the user's ship column
                userCol = input("What column would you like for your ship {} :".format(i+1))
                userName = input("What name would you like for your ship {}?: ".format(i+1))
                
                try:
                    #evaluates the value of userRow and userCol
                    userRow = eval(userRow)
                    userCol = eval(userCol)
                    userName = eval(userName)
                except:
                    #if the above code erros it runs this
                    print("   ")
                    print("That not a valid input try again!")
                    some_bool = True
                if str != type(userRow) and str != type(userCol)and str == type(userName) and (userCol <= gridSize) and (userRow <= gridSize):   
                    some_bool = False
                else:
                    print("   ")
                    print("That not a valid input try again!")
                

            compGuessBoard[userRow][userCol] = "s", userName
            

def get_user_ship_placement(ship_length):
    while True:
        try:
            user_input = input(f"Enter the starting position (e.g., A1) for your {ship_length}-length ship: ").upper()
            if len(user_input) != 2 or not user_input[0].isalpha() or not user_input[1].isdigit():
                raise ValueError()
            row = ord(user_input[0]) - ord('A')
            col = int(user_input[1]) - 1
            if is_valid_placement(guessBoard, row, col, ship_length, 'horizontal'):
                return row, col, 'horizontal'
            elif is_valid_placement(guessBoard, row, col, ship_length, 'vertical'):
                return row, col, 'vertical'
            else:
                print("Invalid placement. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid starting position (e.g., A1).")


        
# function used to print the user's board
def printBoardUser():
    for row in guessBoard:
        for cell in row:
            if cell == 0 or cell == '-' or cell == "s":
                print("0", end=" ")
            else:
                print(cell, end=" ")
        print()

# function used to print the computer's board
def printBoardCpu():
    for row in compGuessBoard:
        for cell in row:
            if cell == 0 or cell == '-' or cell == "s":
                print("0", end=" ")
            else:
                print(cell, end=" ")
        print()

#function used for the computers side of playing
def computerPlay():
    print("--------------------------------------Computer Turn-----------------------------------------------------")
    #prints board
    print("ENEMY BOARD")
    printBoardCpu()

    #amount of turns represented as ammo and ship lives
    ammo = 5
    ships_left = 1
    while ammo>0:
            print("COMPUTER'S TURN")
            
            row = random.randint(1, gridSize)
            column = random.randint(1, gridSize)
            
           
            print("-----------------------------------------------------------------------")
            print("The computer guessed row: {} col: {}".format(row, column))



            #ensures the user cannot type outisde of the bounds of the grid
            if row not in range(1,gridSize+1) or column not in range(1, gridSize+1):
                print("\nThe numbers must be between 1-{}!".format(gridSize))
                ammo-=1
                continue


            row = row - 1 # Reducing number to desired index.
            column = column - 1
            
            
            #checks to see if you shot a spot already  
            if compGuessBoard[row][column] == "-" or compGuessBoard[row][column] == "X":
                print("\nYou have already shot that spot!\n")
                continue
            #compares the list of computer ships and checks to see if choice list matches any of them
            elif compGuessBoard[row][column] == "s":
                print("\nBoom! You hit the {} ship! \n".format(userName))
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
            printBoardCpu()
        
            print("  ")
            # prints your current ammo and ships lives every turn
            print(f"Ammo left: {ammo} | Ships left: {ships_left}")
            print("  ")


#overarching funtion that runs the core process of the game
def play_game():
    print("-----------------------------------USER TURN-----------------------------------------------")
    #prints board
    print("ENEMY BOARD")
    printBoardUser()

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
            elif guessBoard[row][column] == "s":
                print("\nBoom! You hit a the {} ship! \n".format(compName))
                guessBoard[row][column] = "X"
                #if its a hit it loses ammo and a ship dies
                ships_left -= 1
                ammo -= 1
                # if no more ships you win
                if ships_left == 0:
                    print("Congrats, you won! (USER WON)")
                    break
               
            else:
                # prints a - if you miss
                print("\nYou missed!\n")
                guessBoard[row][column] = "-"
                ammo -= 1
            # prints board
            print("ENEMY BOARD")
            printBoardUser()
            
            print("  ")
            # prints your current ammo and ships lives every turn
            print(f"Ammo left: {ammo} | Ships left: {ships_left}")
            print("   ")
            
            if ammo == 0:
                computerPlay()

# runs core fucntion
userChoices()
play_game()