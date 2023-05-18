row, column = [int(x) for x in input().split()]
matrix = []
result = 0

for _ in range(row):
    row_data = [x for x in input().split()]
    matrix.append(row_data)

for i in range(row - 1):
    for j in range(column - 1):
        if matrix[i][j] == matrix[i][j + 1] and matrix[i + 1][j] == matrix[i + 1][j + 1]:
            result += 1

print(result)
