# Step 1: Initialize the battlefield from input
size = int(input())
matrix = []

for _ in range(size):
    curr_row = list(input())
    matrix.append(curr_row)

start_position = (0, 0)
# Step 2: Find Submarine location

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "S":
            start_position = i, j

# Step 3: Initialize the movements

movements = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

# Step 4: Main Loop
start_row, start_col = start_position
matrix[start_row][start_col] = "-"
mine_count = 0
cruiser_count = 0

while True:
    command = input()
    new_row, new_col = movements[command](start_row, start_col)

    if matrix[new_row][new_col] == "*":
        mine_count += 1
        if mine_count == 3:
            print("Mission failed, U-9 disappeared! Last known coordinates "
                  f"[{new_row}, {new_col}]!")
            break
        matrix[new_row][new_col] = "-"

    elif matrix[new_row][new_col] == "C":
        cruiser_count += 1
        if cruiser_count == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers"
                  " of the enemy!")
            break
        matrix[new_row][new_col] = "-"

    start_row, start_col = new_row, new_col

matrix[new_row][new_col] = "S"
[print(''.join(row))for row in matrix]
