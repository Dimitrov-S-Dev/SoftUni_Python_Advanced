
# Initialize the matrix
size = int(input())
racing_num = input()
matrix = []

for _ in range(size):
    row_data = input().split()
    matrix.append(row_data)


car_position = (0, 0)
# Finding the tunnels
tunnels_positions = []

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "T":
            tunnels_positions.append([i, j])

movements = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

# Main Loop
start_row, start_col = car_position
distance_covered = 0

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_num} DNF.")
        matrix[start_row][start_col] = "C"
        break
    distance_covered += 10
    new_r, new_c = movements[command](start_row, start_col)

    if matrix[new_r][new_c] == "T":
        matrix[new_r][new_c] = "."
        distance_covered += 20
        for r, c in tunnels_positions:
            if new_r != r and new_c != c:
                new_r, new_c = r, c
                matrix[new_r][new_c] = "."

    elif matrix[new_r][new_c] == "F":
        matrix[new_r][new_c] = "C"
        print(f"Racing car {racing_num} finished the stage!")
        break

    start_row, start_col = new_r, new_c

print(f"Distance covered {distance_covered} km. ")
[print("".join(row)) for row in matrix]
