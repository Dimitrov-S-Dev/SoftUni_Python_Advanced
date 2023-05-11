number_of_rows, number_of_columns = [int(x) for x in input(", ").split()]
matrix = []
for _ in range(number_of_rows):
    curr_row = [int(x) for x in input().split()]
    matrix.append(curr_row)
