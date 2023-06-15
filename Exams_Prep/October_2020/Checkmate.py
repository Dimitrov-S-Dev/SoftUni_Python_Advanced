def get_quins(mtx, row, col, end=8):
    positions = []

    for i in range(1, end): # checking one of the diagonal
        if row + i in range(end) and col + i in range(end):
            if mtx[row + i][col + i] == "Q":
                positions.append([row + i, col + i])
                break

    for i in range(1, end): # checking other diagonal
        if row - i in range(end) and col - i in range(end):
            if mtx[row - i][col - i] == "Q":
                positions.append([row - i, col - i])
                break

    for i in range(1, end): # checking one of the diagonal
        if row - i in range(end) and col + i in range(end):
            if mtx[row - i][col + i] == "Q":
                positions.append([row - i, col + i])
                break

    for i in range(1, end): # checking one of the diagonal
        if row + i in range(end) and col - i in range(end):
            if mtx[row + i][col - i] == "Q":
                positions.append([row + i, col - i])
                break

    for i in range(1, end): # row on the right
        if col + i in range(end):
            if mtx[row][col + i] == "Q":
                positions.append([row, col + i])
                break

    for i in range(1, end): # row on the left
        if col - i in range(end):
            if mtx[row][col - i] == "Q":
                positions.append([row, col - i])
                break

    for i in range(1, end): # column down
        if row + i in range(end):
            if mtx[row + i][col] == "Q":
                positions.append([row + i, col])
                break

    for i in range(1, end): # column up
        if row - i in range(end):
            if mtx[row - i][col] == "Q":
                positions.append([row - i, col])
                break

    return positions


size = 8
matrix = []

for _ in range(8):
    curr_row = input().split()
    matrix.append(curr_row)

king_row, king_col = (0, 0)

for i in range(8):
    for j in range(8):
        if matrix[i][j] == "K":
            king_row, king_col = (i, j)


positions = get_quins(matrix, king_row, king_col)

if positions:
    for position in positions:
        print(position)
else:
    print("The king is safe!")
