import colorama


colorama.init(autoreset=True)

LEN_BOARD = 3
BOARD = []
USER_1 = colorama.Fore.BLUE + "X" + colorama.Fore.RESET
USER_2 = colorama.Fore.RED + "O" + colorama.Fore.RESET

for _ in range(LEN_BOARD):
    row = []
    for _ in range(LEN_BOARD):
        row.append(" ")

    BOARD.append(row)

user = 1
while True:

    board = []
    for row in BOARD:
        board.append("|".join(row))

    board_str = "\n-----\n".join(board)
    print(board_str)

    coord_1 = input(f"Гравець № {user} введи координати клітинки через пробіл: ")
    X, Y = coord_1.split()

    if user == 1:
        BOARD[int(Y)-1][int(X)-1] = USER_1
        user = 2
    else:
        BOARD[int(Y)-1][int(X)-1] = USER_2
        user = 1
