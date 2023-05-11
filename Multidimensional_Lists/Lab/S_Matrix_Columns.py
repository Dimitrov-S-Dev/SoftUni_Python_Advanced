def get_sum_columns(matr):
    columns = len(matr[0])
    rows = len(matr)
    sum_columns = []

    for i in range(columns):
        curr_sum_column = 0
        for j in range(rows):
            curr_sum_column += matr[j][i]
        sum_columns.append(curr_sum_column)

    return sum_columns


number_of_rows, number_of_columns = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(number_of_rows):
    curr_row = [int(x) for x in input().split()]
    matrix.append(curr_row)


result = get_sum_columns(matrix)

for res in result:
    print(res)
