# Task 1 Initialize the matrix
rows, cols = [int(x) for x in input().split(",")]
matrix = []


for _ in range(rows):
    curr_row = list(input())
    matrix.append(curr_row)


# Task 2 Find start position and cheese_count

start_row, start_col = (0, 0)
cheese_count = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "M":
            start_row, start_col = (i, j)
        elif matrix[i][j] == "C":
            cheese_count += 1

# Task 3 Initialize the Directions

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

matrix[start_row][start_col] = "*"
# Task 4 Main Loop

while True:
    command = input()
    if command == "danger":
        matrix[start_row][start_col] = "M"
        print("Mouse will come back later!")
        break

    new_row, new_col = directions[command](start_row, start_col)

    if new_row not in range(rows) or new_col not in range(cols):
        matrix[start_row][start_col] = "M"
        print("No more cheese for tonight!")
        break

    if matrix[new_row][new_col] == "@":
        continue

    if matrix[new_row][new_col] == "C":
        matrix[new_row][new_col] = "*"
        cheese_count -= 1
        if cheese_count == 0:
            matrix[new_row][new_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[new_row][new_col] == "T":
        matrix[new_row][new_col] = "M"
        print("Mouse is trapped!")
        break

    start_row, start_col = new_row, new_col

[print(''.join(row)) for row in matrix]
