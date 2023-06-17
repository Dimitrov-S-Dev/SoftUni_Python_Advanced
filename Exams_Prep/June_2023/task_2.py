# Task 1 Initialize the matrix
size = int(input())
matrix = []


for _ in range(size):
    curr_row = input().split()
    matrix.append(curr_row)
    print(matrix)

# Task 2 Find start position

start_row, start_col = (0, 0)

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "":
            start_row, start_col = (i, j)


# Task 3 Initialize the Directions

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
}

# Task 4 Main Loop

while True:
    pass



