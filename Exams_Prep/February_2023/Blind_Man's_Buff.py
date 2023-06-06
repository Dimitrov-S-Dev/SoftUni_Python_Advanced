# Step 1: Initialize the matrix from input data
row, col = (int(x) for x in input().split())
matrix = []

for _ in range(row):
    curr_row = input().split()
    matrix.append(curr_row)

# Step 2: Initialize the start position
start_position = (0, 0)

for i in range(row):
    for j in range(col):
        if matrix[i][j] == "B":
            start_position = i, j

# Step 3: Initialize movements
directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}
# Step 4: Create the variables
start_row, start_col = start_position
moves_count = 0
touch_counts = 0
# Step 5: Main Loop

while True:
    command = input()
    if command == "Finish":
        print("Game over!")
        break

    new_row, new_col = directions[command](start_row, start_col)
    if new_row not in range(row) or new_col not in range(col) or matrix[new_row][new_col] == "O":
        continue

    moves_count += 1

    if matrix[new_row][new_col] == "P":
        touch_counts += 1
        matrix[new_row][new_col] = "-"
        if touch_counts == 3:
            print("Game over!")
            break
    start_row, start_col = new_row, new_col

print(f"Touched opponents: {touch_counts} Moves made: {moves_count}")
