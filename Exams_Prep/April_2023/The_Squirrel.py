# Task 1: Initialize Matrix and commands from input
matrix = []
size = int(input())
commands = input().split(", ")

for row in range(size):
    curr_row = list(input())
    matrix.append(curr_row)

# Task 2: Initialize the start position
start_p = (0, 0)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            start_p = row, col

# Initialize the movements and hazelnuts_count

movements = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}
hazelnuts_count = 0
start_row, start_col = start_p

for command in commands:
    new_row, new_col = movements[command](start_row, start_col)
    if new_row in range(size) and new_col in range(size):
        if matrix[new_row][new_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        elif matrix[new_row][new_col] == "h":
            hazelnuts_count += 1
            matrix[new_row][new_col] = "*"
            if hazelnuts_count == 3:
                print("Good job! You have collected all hazelnuts!")
                break
    else:
        print("The squirrel is out of the field.")
        break
    start_row, start_col = new_row, new_col

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_count}")
