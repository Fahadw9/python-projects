# My take on tic-tac-toe

import random          #For Random Computer Move

BreakOut = False            #To break out of infinite loop with break statement
TileData = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]       #TicTacToe Table

def startingInstructions():
    print("By Default You Will Be Selected As X And The Computer As O")
    print("When Prompted Just Input The Location Where You Want To Put The X")

def updateTable():                   # Visualizes The Table
    for r in TileData:
        for c in r:
            print(c,end = " ")
        print()

startingInstructions()
updateTable()

for i in range(5):               #Player Move Locations
    CurrentMove = int(input("Where Do You Want To Put The X: "))
    if CurrentMove < 4:
        TileData[0][CurrentMove - 1] = "X"
    elif CurrentMove < 7:
        TileData[1][CurrentMove - 4] = "X"
    elif CurrentMove < 10:
        TileData[2][CurrentMove - 7] = "X"

    if i == 5:           #To Break Out Of Loop Under All Circumstances
        break

    while BreakOut == False:          #Infinite loop only breakable by the break command after computer move
        ComputerMove = random.randint(0, 2)             # row value
        ComputerMove2 = random.randint(0, 2)            # Column Value

        if TileData[ComputerMove][ComputerMove2] != "X" and "O":
            TileData[ComputerMove][ComputerMove2] = "O"
            break

    updateTable()
