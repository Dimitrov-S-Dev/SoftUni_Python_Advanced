# Read the matrix size
n = int(input())
matrix = []

# Create matrix
for _ in range(n):
    data_row = list(input())
    matrix.append(data_row)

# Locate the submarine, cruisers  and mines
submarine_location = (0, 0)
mines_locations = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "S":
            submarine_location = i, j
        elif matrix[i][j] == "*":
            mines_locations.append((i, j))

# Initialize the movements

movements = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

start_r, start_c = submarine_location
matrix[start_r][start_c] = "-"
battle_cruisers = 3
submarine_hits = 0
# Main Loop
while True:
    command = input()
    new_r, new_c = movements[command](start_r, start_c)
    start_r, start_c = new_r, new_c

    if matrix[new_r][new_c] == "*":
        submarine_hits += 1
        if submarine_hits == 3:
            matrix[new_r][new_c] = "S"
            print(f"Mission failed, U-9 disappeared! "
                  f"Last known coordinates [{new_r}, {new_c}]!")
            break
        else:
            matrix[new_r][new_c] = "-"

    elif matrix[new_r][new_c] == "C":
        matrix[new_r][new_c] = "-"
        battle_cruisers -= 1
        if battle_cruisers == 0:
            matrix[new_r][new_c] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers"
                  " of the enemy!")
            break


[print("".join(row)) for row in matrix]
