# Stage 5: Function to Check Range

def get_range(number, range_num):
    if number not in range(range_num):
        return abs(abs(number) - range_num)
    else:
        return number


# Stage 1: Create matrix from input data
size = int(input())
matrix = []

for _ in range(size):
    row_data = input().split()
    matrix.append(row_data)

# Stage 2: Initialize player coordinates
player_coordinates = (0, 0)

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "P":
            player_coordinates = (i, j)

# Stage 3: Initialize directions

directions = {
    "up": lambda row, col: (row - 1, col),
    "down": lambda row, col: (row + 1, col),
    "left": lambda row, col: (row, col - 1),
    "right": lambda row, col: (row, col + 1),
}

# Stage 4: Main Loop and initialize needed variables
start_r, start_c = player_coordinates
total_coins = 0
paths = [[start_r, start_c]]
while True:
    command = input()
    new_r, new_c = directions[command](start_r, start_c)
    curr_row = get_range(new_r, size)
    curr_col = get_range(new_c, size)
    start_r = curr_row
    start_c = curr_col
    paths.append([curr_row, curr_col])

    if matrix[curr_row][curr_col].isdigit():
        total_coins += int(matrix[curr_row][curr_col])
        matrix[curr_row][curr_col] = "."
        if total_coins >= 100:
            print(f"You won! You've collected {total_coins} coins.")
            break

    elif matrix[curr_row][curr_col] == "X":
        total_coins //= 2
        print(f"Game over! You've collected {total_coins} coins.")
        break

print("Your path:")
[print(path) for path in paths]
