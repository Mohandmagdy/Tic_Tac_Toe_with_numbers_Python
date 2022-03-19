#Hello
print("Hello USERS :)")

#make a board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#starter variables

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]
player = 1
winner = None
game_running = True

#print the board

def printboard(board):
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])

#take the player's input

def playerinput():
    if player == 1:
        print("First player's TURN")
        print("Please enter a number from ", *list1, " and the position of it in seperated lines")
        num = int(input("Number: "))
        pos = int(input("Position: "))
        if pos < 1 or pos > 9:
            print("The position is out of table!!")
        elif num in list1 and board[pos - 1] == "-":
            board[pos - 1] = num
            list1.remove(num)
        elif num not in list1 and board[pos - 1] == "-":
            print("Wrong num!!")
            playerinput()
        elif num in list1 and board[pos - 1] != "-":
            print("Already used place!!")
            playerinput()
        else:
            print("Wrong num and already used place!!")
            playerinput()
    else:
        print("Second player's TURN")
        print("Please enter a number from ", *list2, " and the position of it in seperated lines")
        num = int(input("Number: "))
        pos = int(input("Position: "))
        if pos < 1 or pos > 9:
            print("The position is out of table!!")
        elif num in list2 and board[pos - 1] == "-":
            board[pos - 1] = num
            list2.remove(num)
        elif num not in list2 and board[pos - 1] == "-":
            print("Wrong num!!")
            playerinput()
        elif num in list2 and board[pos - 1] != "-":
            print("Already used place!!")
            playerinput()
        else:
            print("Wrong num and already used place!!")
            playerinput()

#win situatuions

def checkhorizontal(board):
    global winner
    if board[0] != "-" and board[1] != "-" and board[2] != "-":
        if board[0] + board[1] + board[2] == 15:
            winner = str(player)
            return True
    if board[3] != "-" and board[4] != "-" and board[5] != "-":
        if board[3] + board[4] + board[5] == 15:
            winner = str(player)
            return True
    if board[6] != "-" and board[7] != "-" and board[8] != "-":
        if board[6] + board[7] + board[8] == 15:
            winner = str(player)
            return True

def checkvertical(board):
    global winner
    if board[0] != "-" and board[3] != "-" and board[6] != "-":
        if board[0] + board[3] + board[6] == 15:
            winner = str(player)
            return True
    if board[1] != "-" and board[4] != "-" and board[7] != "-":
        if board[1] + board[4] + board[7] == 15:
            winner = str(player)
            return True
    if board[2] != "-" and board[5] != "-" and board[8] != "-":
        if board[2] + board[5] + board[8] == 15:
            winner = str(player)
            return True

def checkdigaonals(board):
    global winner
    if board[0] != "-" and board[4] != "-" and board[8] != "-":
        if board[0] + board[4] + board[8] == 15:
            winner = str(player) 
            return True
    if board[2] != "-" and board[4] != "-" and board[6] != "-":
        if board[2] + board[4] + board[6] == 15:
            winner = str(player)
            return True

#check win

def wonornot():
    global game_running
    if checkdigaonals(board) or checkhorizontal(board) or checkvertical(board):
        printboard(board)
        if player == 1:
            print("The winner is the", winner+ "st player")
        else:
            print("The winner is the", winner+ "nd player")
        game_running = False

#check tie 

def checktie(board):
    global game_running
    if (checkdigaonals(board) or checkhorizontal(board) or checkvertical(board)) and "-" not in board:
        return None
    elif "-" not in board:
        print("It's a DRAW!!")
        game_running = False

#switch the player

def switchplayer():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

#THE GAME

while game_running:
    printboard(board)
    playerinput()
    wonornot()
    checktie(board)
    switchplayer()