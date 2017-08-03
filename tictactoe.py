import random

def start():
    user = raw_input()
    if(user.upper() == "X"):
        return "X"
    elif(user.upper() == "O"):
        return "O"
    else:
        print("Please pick X or O!")
        start()

def generateBoard():
    freshBoard = {"7": " ", "8": " ", "9": " ",
             "4": " ", "5": " ", "6": " ",
             "1": " ", "2": " ", "3": " "}
    return freshBoard
    
def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|"+ board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|"+ board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|"+ board["3"])

def move(userTurn, board):
    userMove = raw_input()
    if(board[userMove] == " "):
        board[userMove] = userTurn
    else:
        print("Sorry! There's already a piece there.  " \
              "Where would you like to move?")
        move(board)

def victory(user, board):
    if((board["7"] == user and board["8"] == user and board["9"] == user) or
       (board["4"] == user and board["5"] == user and board["6"] == user) or
       (board["1"] == user and board["2"] == user and board["3"] == user) or
       
       (board["7"] == user and board["4"] == user and board["1"] == user) or
       (board["8"] == user and board["5"] == user and board["2"] == user) or
       (board["9"] == user and board["6"] == user and board["3"] == user) or

       (board["7"] == user and board["5"] == user and board["3"] == user) or
       (board["1"] == user and board["5"] == user and board["9"] == user)):
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
    print("Welcome to Tic-Tac-Toe!"
          "Do you want to be X or O?")
    turn = start()
    status = 0
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
