n = int(input())
matrix = []
p_diagonal = []
s_diagonal = []

for _ in range(n):
    curr_row = [int(x) for x in input().split(", ")]
    matrix.append(curr_row)

for i in range(n):
    for j in range(n):
        if i == j:
            p_diagonal.append(matrix[i][j])
        if i + j == n - 1:
            s_diagonal.append(matrix[i][j])

print(f"Primary diagonal: {', '.join(str(x) for x in p_diagonal)}. "
      f"Sum: {sum(p_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in s_diagonal)}. "
      f"Sum: {sum(s_diagonal)}")

