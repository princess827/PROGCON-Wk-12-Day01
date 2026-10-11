import random
def checkWinner(board):
    result = "None"
    fillCount = 0
    if board[1] != " " and board[1] == board[2] and board[2] == board[3]:
        result = board[1]
    if board[4] != " " and board[4] == board[5] and board[5] == board[6]:
        result = board[4]
    if board[7] != " " and board[7] == board[8] and board[8] == board[9]:
        result = board[7]
    if board[1] != " " and board[1] == board[4] and board[4] == board[7]:
        result = board[1]
    if board[2] != " " and board[2] == board[5] and board[5] == board[8]:
        result = board[2]
    if board[3] != " " and board[3] == board[6] and board[6] == board[9]:
        result = board[3]
    if board[1] != " " and board[1] == board[5] and board[5] == board[9]:
        result = board[1]
    if board[3] != " " and board[3] == board[5] and board[5] == board[7]:
        result = board[3]
    for k in range(1, 9 + 1, 1):
        if board[k] != " ":
            fillCount = fillCount + 1
    if result == "None" and fillCount == 9:
        result = "Draw"
    
    return result

def computerMove(board):
    valid = False
    while valid == False:
        computerMove = int(random.random() * 9) + 1
        if board[computerMove] == " ":
            valid = True
        else:
            valid = False
    
    return computerMove

def displayBoard(board):
    print(board[1] + " | " + board[2] + " | " + board[3] + chr(13) + board[4] + " | " + board[5] + " | " + board[6] + chr(13) + board[7] + " | " + board[8] + " | " + board[9])

# Main
random.seed()   #Prepare random number generator

board = [""] * (10)

for i in range(1, 9 + 1, 1):
    board[i] = " "
gameOver = False
winner = "None"
r = int(random.random() * 2)
if r == 0:
    currentPlayer = "O"
else:
    currentPlayer = "X"
while gameOver == False:
    displayBoard(board)
    if currentPlayer == "O":
        validMove = False
        while validMove == False:
            print("Enter your move (1-9):")
            playerMove = int(input())
            if playerMove >= 1 and playerMove <= 9:
                if board[playerMove] == " ":
                    validMove = True
                else:
                    print("Space occupied! Try again.")
            else:
                print("Invalid choice! Enter 1-9.")
        board[playerMove] = "O"
    else:
        print("Computer's turn...")
        comMove = computerMove(board)
        board[comMove] = "X"
    winner = checkWinner(board)
    if winner != "None":
        gameOver = True
    else:
        if currentPlayer == "O":
            currentPlayer = "X"
        else:
            currentPlayer = "O"
displayBoard(board)
if winner == "O":
    print("You win!")
else:
    if winner == "X":
        print("Computer wins!")
    else:
        print("It's a draw!")
