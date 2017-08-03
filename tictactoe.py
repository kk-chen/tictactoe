def generateBoard():
    freshBoard = {"topL": " ", "topM": " ", "topR": " ",
             "midL": " ", "midM": " ", "midR": " ",
             "lowL": " ", "lowM": " ", "lowR": " "}
    return freshBoard
    
def printBoard(board):
    print(board["topL"] + "|" + board["topM"] + "|"+ board["topR"])
    print("-+-+-")
    print(board["midL"] + "|" + board["midM"] + "|"+ board["midR"])
    print("-+-+-")
    print(board["lowL"] + "|" + board["lowM"] + "|"+ board["lowR"])

def move(userTurn, board):
    userMove = raw_input()
    if(board[userMove] == " "):
        board[userMove] = userTurn
    else:
        print("Sorry! There's already a piece there.  " \
              "Where would you like to move?")
        move(board)

def victory(user, board):
    if((board["topL"] == user and board["topM"] == user and board["topR"] == user) or
       (board["midL"] == user and board["midM"] == user and board["midR"] == user) or
       (board["lowL"] == user and board["lowM"] == user and board["lowR"] == user) or
       
       (board["topL"] == user and board["midL"] == user and board["lowL"] == user) or
       (board["topM"] == user and board["midM"] == user and board["lowM"] == user) or
       (board["topR"] == user and board["midR"] == user and board["lowR"] == user) or

       (board["topL"] == user and board["midM"] == user and board["lowR"] == user) or
       (board["lowL"] == user and board["midM"] == user and board["topR"] == user)):
        return 1
    else:
        return 0

def nextRound():
    print("Would you like to play again?")
    userPlay = raw_input()
    if(userPlay.lower() == "yes" or userPlay.lower() == "y"):
        gameStart()
    else:
        print("Bye-bye!")
    
def gameStart():
    status = 0
    turn = "X"
    theBoard = generateBoard()
    while(" " in theBoard.values() and status == 0):
        printBoard(theBoard)
        print("It's " + turn + "'s turn.  Where would you like to move?")
        move(turn, theBoard)
        status = victory(turn, theBoard)
        if(status == 1):
            printBoard(theBoard)
            print("Congradulations! " + turn + " won the game!")
            nextRound()
            return
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    printBoard(theBoard)
    print("Sorry! Nobody won")
    nextRound()

gameStart()
