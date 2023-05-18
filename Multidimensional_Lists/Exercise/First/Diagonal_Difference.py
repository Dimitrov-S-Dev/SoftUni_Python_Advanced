size = int(input())
matrix = []
sum_p_diagonal = 0
sum_s_diagonal = 0

for _ in range(size):
    curr_row = [int(x) for x in input().split()]
    matrix.append(curr_row)

for i in range(size):
    sum_p_diagonal += matrix[i][i]
    sum_s_diagonal += matrix[i][size - i - 1]

diff = sum_p_diagonal - sum_s_diagonal
print(abs(diff))
