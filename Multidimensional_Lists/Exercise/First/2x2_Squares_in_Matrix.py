row, column = [int(x) for x in input().split()]
matrix = []
squares = 0

for _ in range(row):
    row_data = [x for x in input().split()]
    matrix.append(row_data)

for row in range(row - 1):
    for col in range(column - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] \
                == matrix[row + 1][col + 1]:
            squares += 1

print(squares)



