def check_range(board, first_row, other_row):
    return abs(first_row - other_row) == 1


def get_player_position(board, symbol):
    for row in range(ROWS_COUNT):
        for col in range(COLS_COUNT):
            if board[row][col] == symbol:
                return row, col


ROWS_COUNT = 8
COLS_COUNT = 8

matrix = [input().split() for _ in range(ROWS_COUNT)]

wr, wc = get_player_position(matrix, "w")
br, bc = get_player_position(matrix, "b")
cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = [8, 7, 6, 5, 4, 3, 2, 1]

movements = {
    "white": lambda r, c: (r - 1, c),
    "black": lambda r, c: (r + 1, c),
}

game_over = False

if abs(wc - bc) == 1:
    if check_range(matrix, wc, bc):
        if wr < br:
            print(f"Game over! White win, capture on {cols[wc]}{rows[wr]}.")
        else:
            print(f"Game over! Black win, capture on {cols[bc]}{rows[br]}.")
        game_over = True

while not game_over:
    wr, wc = movements["white"](wr, wc)
    if wr == 0:
        print(f"Game over! White pawn is promoted to a queen at {cols[wc]}{rows[wr]}.")
        break
    br, bc = movements["black"](br, bc)
    if br == 7:
        print(f"Game over! Black pawn is promoted to a queen at {cols[bc]}{rows[br]}.")
        break

