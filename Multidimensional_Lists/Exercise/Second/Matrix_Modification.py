size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command, *data = input().split()
    if command == "END":
        break

    row, col, value = [int(x) for x in data]
    if row not in range(size) or col not in range(size):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")

