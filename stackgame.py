import os

# End the game
def endGame():
    print("Thanks for playing!")
    os._exit(0)

# Recursively find the minimum number of moves required to win
def minMoves(max):
    if(max == 1):
        return 1
    # User needs to move every disc on top of bottom one off, then move bottom,
    # then move everything else back on.
    return 2*minMoves(max-1) + 1

# Draw the board.
def draw(p1, p2, p3):
    # This is the total number of discs.
    max = len(p1) + len(p2) + len(p3) - 1

    print()
    for i in range(max+1):
        for p in [p1, p2, p3]:
            # Print the pillar item at this index. Otherwise print pipe to
            # represent a segment of the pillar.
            try:
                print(p[max-i], end="\t")
            except:
                print("|", end="\t")
        print()

# Initialize the board.
def initBoard(max):
    # Each array represents a pillar of the board.
    p1 = []
    p2 = []
    p3 = []

    #Populate the first pillar with numbers to represent disc size.
    for i in range(max):
        p1.append(max-i)

    return p1, p2, p3

# Check to see if the move the user attempted to make is valid.
def checkValidMove(p1, p2, p3, a, b):
    pillars = [p1, p2, p3]

    # If the user tried to move a disc to the pillar it is currently on or the user
    # tried to move from an empty pillar, the move is invalid.
    if a == b or len(pillars[a]) == 0:
        return False
    # If the user tried to move to an empty pillar, the move is valid.
    elif len(pillars[b]) == 0:
        return True
    # If the user tried to move a disc onto a smaller disc, the move is invalid.
    elif pillars[a][len(pillars[a])-1] > pillars[b][len(pillars[b])-1]:
        return False
    else:
        return True

# Execute the user's move on the pillars.
def makeMove(p1, p2, p3, a, b):
    pillars = [p1, p2, p3]
    # Remove the disc at the top of Pillar A and put it on Pillar B.
    pillars[b].append(pillars[a].pop())
    return p1, p2, p3

# Allow the user to make a move.
def turn(p1, p2, p3):
    success = False

    # Repeat as long as a valid move has not been made.
    while(not success):
        try:
            # Account for user entering 0 to end game early
            a = int(input("Move from pillar (1-3): ")) - 1
            if(a == -1):
                endGame()

            b = int(input("To pillar (1-3): ")) - 1
            if(b == -1):
                endGame()

            # If a valid move has been selected, make the move and end the loop.
            if checkValidMove(p1, p2, p3, a, b):
                success = True
                p1, p2, p3 = makeMove(p1, p2, p3, a, b)
            else:
                print("Invalid move.")
        except:
            pass
    return p1, p2, p3

# Check to see if the user has won.
def checkWin(p1, p2, p3):
    # If all of the discs have been moved to another pillar, the user has won.
    if (len(p1) == 0 and len(p3) == 0) or (len(p1) == 0 and len(p2) == 0):
        return True
    else:
        return False

# Run the game
def run(n):
    turns = 0
    p1, p2, p3 = initBoard(n)

    # Continue playing until the user wins.
    while not checkWin(p1, p2, p3):
        draw(p1, p2, p3)
        p1, p2, p3 = turn(p1, p2, p3)
        turns += 1

    draw(p1, p2, p3)
    print("You won in {} turns!".format(turns))

    # Check to see how user's number of moves compares to minimum number of moves.
    if(turns == minMoves(n)):
        print("Great job, you beat the game in the fewest turns possible!")
    else:
        print("You took " + str(turns-minMoves(n)) + " more turns than you needed to.")


if __name__ == "__main__":
    print("The object of this game is to move all discs from one pillar to another.")
    print("You may not place a disc on top of a smaller disc and you may not move ")
    print("more than one disc at a time. To play, you must select a pillar to move")
    print("from (Pillar A) and a pillar to move to (Pillar B). If your entered")
    print("move is valid, the top disc from Pillar A will be moved to Pillar B.")
    print("Once all discs are on a different pillar than the initial one, you win!")
    print("Enter \"0\" at any time to stop playing.")
    print()

    n = int(input("Enter the number of discs do you wish to play with: "))
    if(n <= 0):
        endGame()

    print("\nA game of " + str(n) + " discs can be completed in " + str(minMoves(n)) + " moves. Good luck!")
    run(n)
