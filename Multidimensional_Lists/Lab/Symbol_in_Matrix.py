n = int(input())

matrix = []

for row in range(n):
    curr_row = list(input())
    matrix.append(curr_row)

sbl = input()
inx = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == sbl:
            inx.append((i, j))

if inx:
    for symbol in inx:
        print(symbol)
else:
    print(f"{sbl} does not occur in the matrix")
