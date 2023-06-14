rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    curr_row = input().split()
    matrix.append(curr_row)

start_row, start_col = (0, 0)
items_count = 0


for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "Y":
            start_row, start_col = (i, j)
        elif matrix[i][j] not in [".", "Y"]:
            items_count += 1


matrix[start_row][start_col] = "x"

directions = {
    "up": lambda r, c: ((r - 1 if r - 1 >= 0 else rows - 1), c),
    "down": lambda r, c: ((r + 1) % rows, c),
    "left": lambda r, c: (r, (c - 1 if c - 1 >= 0 else cols - 1)),
    "right": lambda r, c: (r, (c + 1) % cols),
}

collections = {
    "D": [0, "Christmas decorations"],
    "G": [0, "Gifts"],
    "C": [0, "Cookies"],
}

all_collected = False
while True:
    data = input().split("-")
    command = data[0]
    if command == "End":
        matrix[start_row][start_col] = "Y"
        break
    steps = int(data[1])
    for _ in range(steps):
        new_row, new_col = directions[command](start_row, start_col)
        start_row, start_col = new_row, new_col

        if matrix[new_row][new_col] in ["D", "C", "G"]:
            element = matrix[new_row][new_col]
            collections[element][0] += 1
            items_count -= 1
            if items_count == 0:
                print("Merry Christmas!")
                matrix[new_row][new_col] = "Y"
                all_collected = True
                break
        if not all_collected:
            matrix[new_row][new_col] = "x"

    if all_collected:
        break


print("You've collected:")
for value in collections.values():
    print(f"- {value[0]} {value[1]}")

[print(" ".join(row)) for row in matrix]

