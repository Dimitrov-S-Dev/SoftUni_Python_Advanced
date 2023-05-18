def is_outside(row, col, rows, cols):
    return row not in range(rows) and col not in range(cols)


row, column = [int(x) for x in input().split()]
matrix = []

for _ in range(row):
    matrix.append(int(x) for x in input().split())

while True:
    command = input()
    if command == "END":
        break
    line_parts = command.split()
    if line_parts[0] != "swap" or len(line_parts) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]
    if is_outside(row1, col1, row, column) or is_outside(row2, col2, row, column):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row, sep=" ")

