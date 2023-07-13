import random

#creates board
guessBoard = [["x"] * 5 for i in range(5)]


#prints board
def printBoard():
    print(guessBoard)


#returns the random location in the grid 
def randomShips():
    randomRow1 = random.randrange(1,5)
    randomCol1 = random.randrange(1,5)
    
    location1 = guessBoard[randomRow1][randomCol1]

    randomRow2 = random.randrange(1,5)
    randomCol2 = random.randrange(1,5)
    
    location2 = guessBoard[randomRow2][randomCol2]

    randomRow3 = random.randrange(1,5)
    randomCol3 = random.randrange(1,5)
    
    location3 = guessBoard[randomRow3][randomCol3]
    
    print(guessBoard)
    
    return location1, location2, location3

def shipHit():
    pass

def shipMissed():
    pass

def shipSunk():
    pass


randomShips()

#prints the list of lists in a grid format
print('\n'.join(' '.join(map(str,sl)) for sl in guessBoard))


