# row, column = [int(x) for x in input().split()]
# matrix = []
# max_sum = 0
#
# for _ in range(row):
#     matrix.append([int(x) for x in input().split()])
#
# best_sum = float("-inf")
# start_row = 0
# start_col = 0
# for row in range(row - 2):
#     for col in range(column - 2):
#         curr_sum = matrix[row][col] + matrix[row][col + 1] +\
#                    matrix[row][col + 2] + matrix[row + 1][col] +\
#                    matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +\
#                    matrix[row + 2][col] + matrix[row + 2][col + 1] +\
#                    matrix[row + 2][col + 2]
#         if curr_sum > best_sum:
#             best_sum = curr_sum
#             start_row = row
#             start_col = col
#
# print(f"Sum = {best_sum}")
# print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
# print(f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}")
# print(f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}")
#

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = float("-inf")
max_sum_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_line = matrix[row][col:col + 3]
        second_line = matrix[row + 1][col:col + 3]
        third_line = matrix[row + 2][col:col + 3]

        curr_sum = sum(first_line + second_line + third_line)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_matrix = [first_line, second_line, third_line]

print(f"Sum = {max_sum}")
for row in max_sum_matrix:
    print(*row, sep=" ")
