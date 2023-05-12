def find_symbol(matrix, symbol):
    for row_index in range(n):
        for column_index in range(n):
            if matrix[row_index][column_index] == sbl:
                return row_index, column_index
    return None


n = int(input())
matrix = [list(input()) for _ in range(n)]

sbl = input()
result = find_symbol(matrix, sbl)

if result:
    row_index, column_index = result
    print(f"({row_index}, {column_index})")
else:
    print(f"{sbl} does not occur in the matrix")
