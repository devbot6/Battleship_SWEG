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


