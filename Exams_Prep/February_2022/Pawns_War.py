def get_white_range(matrix, row, col):
    ranges = {
        (row + 1, col - 1),
        (row + 1, col + 1),
    }
    for r, c in ranges:
        if r in range(8) and c in range(8) and matrix[r][c] == "w":
            return True
    return False


def get_black_range(matrix, row, col):
    ranges = {
        (row - 1, col - 1),
        (row - 1, col + 1),
    }
    for r, c in ranges:
        if r in range(8) and c in range(8) and matrix[r][c] == "b":
            return True
    return False


# Step 1: Read the data and create the board
board = []
for _ in range(8):
    row_data = input().split()
    board.append(row_data)

# Step 2: Initialize the positions and their names
white_position = 0, 0
black_position = 0, 0
cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = [8, 7, 6, 5, 4, 3, 2, 1]

# Step 3: Find positions
for i in range(8):
    for j in range(8):
        if board[i][j] == "w":
            white_position = (i, j)
        elif board[i][j] == "b":
            black_position = (i, j)

# Step 4: Initialize movements
movements = {
    "white": lambda r, c: (r - 1, c),
    "black": lambda r, c: (r + 1, c),
}

# Step 5: Main Loop
wr, wc = white_position
br, bc = black_position


while True:
    if abs(wc - bc) == 1:
        if get_white_range(board, br, bc):
            print(f"Game over! White win, capture on {cols[bc]}{rows[br]}.")
            break

        wr, wc = movements["white"](wr, wc)

        if get_black_range(board, wr, wc):
            print(f"Game over! Black win, capture on {cols[wc]}{rows[wr]}.")
            break
        br, bc = movements["black"](br, bc)

    else:

        wr, wc = movements["white"](wr, wc)
        if wr == 0:
            print(f"Game over! White pawn is promoted to a queen at "
                  f"{cols[wc]}{rows[wr]}.")
            break
        br, bc = movements["black"](br, bc)
        if br == 7:
            print(f"Game over! Black pawn is promoted to a queen at "
                  f"{cols[bc]}{rows[br]}.")
            break

