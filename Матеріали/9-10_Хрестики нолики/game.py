import colorama


colorama.init(autoreset=True)


LEN_BOARD = 3
BOARD = []
for _ in range(LEN_BOARD):
    row = []
    for _ in range(LEN_BOARD):
        row.append(" ")

    BOARD.append(row)

USER_1 = colorama.Fore.RED + "O" + colorama.Fore.RESET
USER_2 = colorama.Fore.BLUE + "X" + colorama.Fore.RESET

is_first_user_next = True

while True:
    board = ""
    for row in BOARD:
        board += "|" + "|".join(row) + "|"
        board += "\n-------\n"

    print(board)

    for row in BOARD:
        if "".join(row) in [USER_1 * LEN_BOARD, USER_2 * LEN_BOARD]:
            print(f"Гравець № {1 if not is_first_user_next else 2} виграв")
            quit()

    for i in range(LEN_BOARD):
        line = ""
        for row in BOARD:
            line += row[i]

        if line in [USER_1 * LEN_BOARD, USER_2 * LEN_BOARD]:
            print(f"Гравець № {1 if not is_first_user_next else 2} виграв")
            quit()

    if BOARD[0][0] + BOARD[1][1] + BOARD[2][2] in [USER_1 * LEN_BOARD, USER_2 * LEN_BOARD]  or BOARD[0][2] + BOARD[1][1] + BOARD[2][0] in [USER_1 * LEN_BOARD, USER_2 * LEN_BOARD]:
        print(f"Гравець № {1 if not is_first_user_next else 2} виграв")
        quit()

    user_coord = input(f"Гравець № {1 if is_first_user_next else 2} введи координати ходу через пробіл, наприклад '1 2': ")
    x, y = user_coord.split()

    if BOARD[int(y) - 1][int(x) - 1] != " ":
        print(colorama.Back.RED + "Ця клітинка зайнята\n" + colorama.Back.RESET)
        continue

    if is_first_user_next:
        is_first_user_next = False
        BOARD[int(y) - 1][int(x) - 1] = USER_1
    else:
        is_first_user_next = True
        BOARD[int(y) - 1][int(x) - 1] = USER_2


