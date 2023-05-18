# size = int(input())
# matrix = []
# p_diagonal = []
# s_diagonal = []
#
# for _ in range(size):
#     curr_row = [int(x) for x in input().split(", ")]
#     matrix.append(curr_row)
#
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             p_diagonal.append(matrix[i][j])
#         if i + j == size - 1:
#             s_diagonal.append(matrix[i][j])
#
# print(f"Primary diagonal: {', '.join(str(x) for x in p_diagonal)}. "
#       f"Sum: {sum(p_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in s_diagonal)}. "
#       f"Sum: {sum(s_diagonal)}")

size = int(input())
matrix = []
p_diagonal = []
s_diagonal = []

for _ in range(size):
    curr_row = [int(x) for x in input().split(", ")]
    matrix.append(curr_row)

for i in range(size):
    p_diagonal.append(matrix[i][i])
    s_diagonal.append(matrix[i][size - 1 - i])

print(f"Primary diagonal: {', '.join(str(x) for x in p_diagonal)}. "
      f"Sum: {sum(p_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in s_diagonal)}. "
      f"Sum: {sum(s_diagonal)}")


