text = input()
size = int(input())
matrix = []

for _ in range(size):
    curr_row = list(input())
    matrix.append(curr_row)

start_row, start_col = (0, 0)


for i in range(size):
    for j in range(size):
        if matrix[i][j] == "P":
            start_row, start_col = (i, j)

matrix[start_row][start_col] = "-"
directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

commands_count = int(input())
for _ in range(commands_count):
    command = input()
    new_row, new_col = directions[command](start_row, start_col)

    if new_row not in range(size) or new_col not in range(size):
        if text:
            text = text[:-1]
        continue

    if matrix[new_row][new_col] != "-":
        text += matrix[new_row][new_col]
        matrix[new_row][new_col] = "-"

    start_row, start_col = new_row, new_col

matrix[start_row][start_col] = "P"
print(text)
[print(''.join(row)) for row in matrix]
