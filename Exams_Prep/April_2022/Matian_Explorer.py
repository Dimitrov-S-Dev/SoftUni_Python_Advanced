SIZE = 6
matrix = []
start_row, start_col = (0, 0)

for _ in range(SIZE):
    curr_row = input().split()
    matrix.append(curr_row)

for i in range(SIZE):
    for j in range(SIZE):
        if matrix[i][j] == "E":
            start_row, start_col = (i, j)


commands = input().split(", ")

directions = {
    "up": lambda x, y: ((x - 1 if x - 1 in range(SIZE) else 5), y),
    "down": lambda x, y: ((x + 1 if x + 1 in range(SIZE) else 0), y),
    "left": lambda x, y: (x, (y - 1 if y - 1 in range(SIZE) else 5)),
    "right": lambda x, y: (x, (y + 1 if y + 1 in range(SIZE) else 0)),
}

print_deposits = {
    "W": "Water deposit found at",
    "M": "Metal deposit found at",
    "C": "Concrete deposit found at",
}
deposits = set()

for command in commands:
    new_row, new_col = directions[command](start_row, start_col)

    if matrix[new_row][new_col] == "R":
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

    elif matrix[new_row][new_col] != "-":
        element = matrix[new_row][new_col]
        print(f"{print_deposits[element]} ({new_row}, {new_col})")
        deposits.add(element)

    start_row, start_col = new_row, new_col

if len(deposits) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

