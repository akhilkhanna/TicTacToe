over = 0
win = 0
board = ['#', "1", "2", "3", "4", "5", "6", "7", "8", "9",]

def print_board():
    print("\n" * 10)
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])

def get_location(name,symbol):
    flag = 0
    while flag == 0:
        print("\n\n")
        loc = int(input(f"IT'S {name}'S TURN! WHERE DO YOU WANT TO PLACE FROM [1-9]: "))
        if board[loc] == '✘' or board[loc] == '𝙊':
            print("SOMEONE ALREADY PLAYED THAT LOCATION! ENTER AGAIN")
        else:
            board[loc] = symbol
            flag = 1


def check_win(name,symbol):
    if (board[1] == board[2] == board[3] == symbol) or (board[4] == board[5] == board[6] == symbol) or(board[7] == board[8] == board[9] == symbol) or (board[1] == board[4] == board[7] == symbol) or(board[2] == board[5] == board[8] == symbol) or (board[3] == board[6] == board[9] == symbol) or (board[1] == board[5] == board[9] == symbol) or (board[3] == board[5] == board[7] == symbol):
        win = 1
        over = 1
        print(f"{name} WON THE GAME!")
        exit()

def check_tie():
    if play >= 8:
        over = 1
        print("IT IS A TIE")
        exit()

play = 0
print("WELCOME TO TIC TAC TOE GAME!\n")
userx = input("ENTER NAME OF PLAYER CHOOSING ✘: ")
usero = input("ENTER NAME OF PLAYER CHOOSING 𝙊: ")
print("\nRULES TO PLAY: \n\tENTER THE VALUE OF THE LOCATION AS SHOWN ON THE BOARD TO PLACE YOUR INPUT IN IT")
print_board()
while over == 0:
    if play%2 == 0:
        get_location(userx,'✘')
        print_board()
        check_win(userx,'✘')
        check_tie()
        play += 1
    else:
        get_location(usero,'𝙊')
        print_board()
        check_win(usero,'𝙊')
        check_tie()
        play += 1

