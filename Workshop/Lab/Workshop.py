from collections import deque

player_one_symbol = "1"
player_two_symbol = "2"

rows, cols = 6, 7

turn = deque([[1, player_one_symbol], [2, player_two_symbol]])
board = [["0"] * cols for _ in range(rows)]

directions = {
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
}

while True:
    [print(f" {', '.join(row)}") for row in board]
    player_num, player_symbol = turn.popleft()
    player_col = int(input(f"\nPlayer {player_num}, please choose a column:")) - 1

    if player_col not in range(cols):
        print(f"Select a valid number in range ({1} {cols})")
        continue

    row = 0
    if board[row][player_col] != "0":
        print(f"No empty spaces on that row!")
        continue

    while True:
        row += 1
        if row == rows - 1 or board[row + 1] != "0":
            board[row][player_col] = player_symbol
            break

    for move in directions:
        r, c = row, player_col

        for _ in range(3):
            r, c = r + move[0], c + move[1]

            if r not in range(rows) and c not in range(cols):
                break

            if board[r][c] != player_symbol:
                break
        else:
            [print(f"[ {', '.join(row)}]") for row in board]
            print(f"The winner is player: {player_num}")
            raise SystemExit

    turn.append(turn.popleft())






