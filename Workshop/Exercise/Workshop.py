def check_for_win():
    player_name, player_symbol = players[0]
    size = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - i - 1] == player_symbol for i in range(size)])
    row_win = any([all(True if pos == player_symbol else False for pos in row)for row in board])
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size))for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit
    players.append(players.pop())
    choose_position()


def place_symbol(position):
    row, col = (position - 1) // 3, (position - 1) % 3

    board[row][col] = players[0][1]
    check_for_win()
    print_board()
    choose_position()


def choose_position():
    while True:
        position = input(f"{players[0][0]} choose a position [1-9]: ")

        if any([True if position in row else False for row in board]):
            break
        else:
            print(f"{players[0][0]} please select a valid position!")

    place_symbol(int(position))


def print_board(begin=False):
    if begin:
        print(f"This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")

    while True:
        player_one_symbol = input(f"{player_one_name} "
                                  f"would you like to play with X or 0").upper()
        if player_one_symbol not in "XO":
            print(f"{player_one_name} please select a valid option")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    choose_position()


players = []
board = [[str(i), str(i + 1), str(i + 2)]for i in range(1, 10, 3)]
start()