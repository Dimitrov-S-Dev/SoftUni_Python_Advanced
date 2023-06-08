# Stage 4: Create direction function
def get_direction(matrix, row, col, sub_command, value):
    if sub_command == "Create":
        if matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = value[1]

    elif sub_command == "Update":
        if matrix[row][col].isalnum():
            matrix[row][col] = value[1]

    elif sub_command == "Delete":
        if matrix[row][col].isalnum():
            matrix[row][col] = "."

    elif sub_command == "Read":
        if matrix[row][col].isalnum():
            print(matrix[row][col])

    return matrix


# Stage 1: Initialize matrix and start position from input
size = 6
matrix = []

for _ in range(size):
    curr_row = input().split()
    matrix.append(curr_row)

# Stage 2: Get the starting position from input
start_row, start_col = [int(x) for x in input().strip("()").split(", ")]

# Stage 3: Initialize directions
directions = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),
}
# Stage 4: Main Loop

while True:
    command, *args = input().split(", ")
    if command == "Stop":
        break
    new_row, new_col = directions[args[0]](start_row, start_col)
    start_row, start_col = new_row, new_col

    matrix = get_direction(matrix, new_row, new_col, command,args)

[print(" ".join(row)) for row in matrix]
