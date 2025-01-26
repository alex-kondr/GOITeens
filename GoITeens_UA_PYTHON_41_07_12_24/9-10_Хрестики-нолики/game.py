import colorama
import random
X = random.randint(0, 2)
Y = random.randint(0, 2)


colorama.init(autoreset=True)

LEN_BOARD = 3
BOARD = []
BOARD_REVERSE = []
USER_1 = colorama.Fore.BLUE + "X" + colorama.Fore.RESET
USER_2 = colorama.Fore.RED + "O" + colorama.Fore.RESET

for _ in range(LEN_BOARD):
    row = []
    for _ in range(LEN_BOARD):
        row.append(" ")

    BOARD.append(row)
    BOARD_REVERSE.append(row.copy())

user = 1
while True:
    board = []
    for row in BOARD:
        board.append("|".join(row))

    board_str = "\n-----\n".join(board)
    print(board_str)

    if [USER_1] * LEN_BOARD in BOARD or [USER_2] * LEN_BOARD in BOARD:
        print(f"\nГравець № {1 if user == 2 else 2} виграв!\n")
        break

    for i in range(LEN_BOARD):
        for j in range(LEN_BOARD):
            BOARD_REVERSE[i][j] = BOARD[j][i]

    if [USER_1] * LEN_BOARD in BOARD_REVERSE or [USER_2] * LEN_BOARD in BOARD_REVERSE:
        print(f"\nГравець № {1 if user == 2 else 2} виграв!\n")
        break

    if [BOARD[0][0], BOARD[1][1], BOARD[2][2]] in [[USER_1] * LEN_BOARD, [USER_2] * LEN_BOARD]\
        or [BOARD[0][2], BOARD[1][1], BOARD[2][0]] in [[USER_1] * LEN_BOARD, [USER_2] * LEN_BOARD]:
        print(f"\nГравець № {1 if user == 2 else 2} виграв!\n")
        break

    coord_1 = input(f"\nГравець № {user} введи координати клітинки через пробіл: ")
    X, Y = coord_1.split()

    if BOARD[int(Y)-1][int(X)-1] != " ":
        print(colorama.Fore.RED + "\nДана клітинка вже зайнята, введіть інші координати клітинки\n")
        continue

    if user == 1:
        BOARD[int(Y)-1][int(X)-1] = USER_1
        user = 2
    else:
        BOARD[int(Y)-1][int(X)-1] = USER_2
        user = 1
