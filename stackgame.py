def draw(p1, p2, p3):
    max = len(p1) + len(p2) + len(p3) - 1

    print()
    for i in range(max+1):
        for p in [p1, p2, p3]:
            try:
                print(p[max-i], end="\t")
            except:
                print("|", end="\t")
        print()

def initBoard(max):
    p1 = []
    p2 = []
    p3 = []

    for i in range(max):
        p1.append(max-i)

    return p1, p2, p3

def checkValidMove(p1, p2, p3, a, b):
    pillars = [p1, p2, p3]

    if a == b or len(pillars[a]) == 0:
        return False
    elif len(pillars[b]) == 0:
        return True
    elif pillars[a][len(pillars[a])-1] > pillars[b][len(pillars[b])-1]:
        return False
    else:
        return True

def makeMove(p1, p2, p3, a, b):
    pillars = [p1, p2, p3]
    pillars[b].append(pillars[a].pop())
    return p1, p2, p3

def turn(p1, p2, p3):
    success = False
    while(not success):
        try:
            a = int(input("Move from pillar (1-3): ")) - 1
            b = int(input("To pillar (1-3): ")) - 1
        except:
            pass
        if checkValidMove(p1, p2, p3, a, b):
            success = True
            p1, p2, p3 = makeMove(p1, p2, p3, a, b)
        else:
            print("Invalid move.")
    return p1, p2, p3

def checkWin(p1, p2, p3):
    if (len(p1) == 0 and len(p3) == 0) or (len(p1) == 0 and len(p2) == 0):
        return True
    else:
        return False

def run(n):
    turns = 0

    p1, p2, p3 = initBoard(n)
    while not checkWin(p1, p2, p3):
        draw(p1, p2, p3)
        p1, p2, p3 = turn(p1, p2, p3)
        turns += 1
    draw(p1, p2, p3)
    print("You won in {} turns!".format(turns))


if __name__ == "__main__":
    print("The object of this game is to move all discs from one pillar to another.")
    print("You may not place a disc on top of a smaller disc and you may not move ")
    print("more than one disc at a time. To play, you must select a pillar to move")
    print("from (Pillar A) and a pillar to move to (Pillar B). If your entered")
    print("move is valid, the top disc from Pillar A will be moved to Pillar B.")
    print("Once all discs are on a different pillar than the initial one, you win!")
    print()
    n = int(input("Enter the number of discs do you wish to play with: "))
    run(n)
