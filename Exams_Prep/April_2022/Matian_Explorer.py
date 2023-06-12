# Read the field and commands
field = [input().split() for _ in range(6)]
commands_list = input().split(", ")

# Initialize command move
commands_map = {
    "up": lambda r, c: ((r - 1 if r - 1 in range(6) else 5), c),
    "down": lambda r, c: ((r + 1 if r + 1 in range(6) else 0), c),
    "left": lambda r, c: (r, (c - 1 if c - 1 in range(6) else 5)),
    "right": lambda r, c: (r, (c + 1 if c + 1 in range(6) else 0)),
}

# Finding the rover and other position
rover_position = 0, 0

for row in range(6):
    for col in range(6):
        if field[row][col] == "E":
            rover_position = (row, col)

# Main loop
current_row, current_col = rover_position
suitable = set()

for command in commands_list:
    new_r, new_c = commands_map[command](current_row, current_col)
    current_row, current_col = new_r, new_c
    if field[new_r][new_c] == "W":
        suitable.add("W")
        print(f"Water deposit found at {(new_r, new_c)}")

    elif field[new_r][new_c] == "M":
        suitable.add("M")
        print(f"Metal deposit found at {(new_r, new_c)}")

    elif field[new_r][new_c] == "C":
        suitable.add("C")
        print(f"Concrete deposit found at {(new_r, new_c)}")

    elif field[new_r][new_c] == "R":
        print(f"Rover got broken at {(new_r, new_c)}")
        break


if len(suitable) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
