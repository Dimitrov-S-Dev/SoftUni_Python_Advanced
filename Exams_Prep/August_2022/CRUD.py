# Initialize the matrix 6 X 6
SIZE = 6
matrix = []

for _ in range(SIZE):
    row_data = input().split()
    matrix.append(row_data)

starting_position = input()
start_row, start_col = int(starting_position[1]), int(starting_position[4])

# Initialize Directions

directions = {
    "up": lambda row, col: (row - 1, col),
    "down": lambda row, col: (row + 1, col),
    "left": lambda row, col: (row, col - 1),
    "right": lambda row, col: (row, col + 1),
}
# Main Loop

while True:
    command = input()
    if command == "Stop":
        break
    sub_command = command.split(", ")

    new_r, new_c = directions[sub_command[1]](start_row, start_col)
    start_row, start_col = new_r, new_c

    if sub_command[0] == "Create" and matrix[new_r][new_c] == ".":
        matrix[new_r][new_c] = sub_command[2]

    elif sub_command[0] == "Update" and matrix[new_r][new_c].isalnum():
        matrix[new_r][new_c] = sub_command[2]

    elif sub_command[0] == "Delete" and matrix[new_r][new_c].isalnum():
        matrix[new_r][new_c] = "."

    elif sub_command[0] == "Read" and matrix[new_r][new_c].isalnum():
        print(matrix[new_r][new_c])

[print(" ".join(row)) for row in matrix]
