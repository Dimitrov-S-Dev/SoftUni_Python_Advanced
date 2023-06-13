def check_position(row, col):
    positions = {
        1: lambda x, y: (x - 1, y - 1),
        2: lambda x, y: (x - 1, y + 1),
        3: lambda x, y: (x + 1, y - 1),
        4: lambda x, y: (x + 1, y + 1),
    }
    for position in positions:
        new_row, new_col = positions[position](row, col)
        if new_row in range(SIZE) and new_col in range(SIZE) and matrix[new_row][new_col] != "-":
            return True
    return False


def get_winner(white_row, white_col, black_row, black_col):
    if white_row <= (SIZE - black_row) - 1:
        print(f"Game over! White pawn is promoted to a queen at {cols[white_col]}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {cols[black_col]}1.")


def get_capture(white_row, white_col, black_row, black_col):
    moves = {
        "white": lambda x, y: (x - 1, y),
        "black": lambda x, y: (x + 1, y),
    }

    if white_row <= black_row:
        get_winner(white_row, white_col, black_row, black_col)
    else:
        while True:
            if check_position(black_row, black_col):
                print(f"Game over! White win, capture on {cols[black_col]}{rows[black_row]}.")
                break
            white_row, white_col = moves["white"](white_row, white_col)

            if check_position(white_row, white_col):
                print(f"Game over! Black win, capture on {cols[white_col]}{rows[white_row]}.")
                break
            black_row, black_col = moves["black"](black_row, black_col)


SIZE = 8
matrix = []

for _ in range(SIZE):
    curr_row = input().split()
    matrix.append(curr_row)

w_r, w_c = (0, 0)
b_r, b_c = (0, 0)

for i in range(SIZE):
    for j in range(SIZE):
        if matrix[i][j] == "w":
            w_r, w_c = (i, j)
        elif matrix[i][j] == "b":
            b_r, b_c = (i, j)

cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = [8, 7, 6, 5, 4, 3, 2, 1]

diff = abs(b_c - w_c)

if diff != 1:
    get_winner(w_r, w_c, b_r, b_c)
else:
    get_capture(w_r, w_c, b_r, b_c)


