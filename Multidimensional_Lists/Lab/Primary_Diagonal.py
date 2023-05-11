def get_matrix(number_row):
    mtx = []

    for _ in range(number_row):
        curr_row = [int(x) for x in input().split()]
        mtx.append(curr_row)
    return mtx


def get_diagonal(mtx):
    diagonal = [mtx[i][i] for i in range(len(mtx))]

    return diagonal


n = int(input())
matrix = get_matrix(n)
result = get_diagonal(matrix)
print(sum(result))
