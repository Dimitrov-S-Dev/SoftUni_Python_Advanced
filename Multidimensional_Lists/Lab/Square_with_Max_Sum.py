import sys
# Read matrix size
rows, columns = map(int, input().split(", "))

# Read matrix elements
matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

# Find the max Sub_matrix
max_sum = - sys.maxsize
max_sub_matrix = []

for i in range(rows - 1):
    for j in range(columns - 1):
        sub_matrix = [
            [matrix[i][j], matrix[i][j+1]],
            [matrix[i+1][j], matrix[i+1][j+1]]
        ]
        sub_matrix_sum = sum(sum(row) for row in sub_matrix)
        if sub_matrix_sum > max_sum:
            max_sum = sub_matrix_sum
            max_sub_matrix = sub_matrix

# Print the result

for row in max_sub_matrix:
    print(*row)
print(max_sum)
