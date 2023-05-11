def get_matrix():
    number_of_rows, number_of_columns = map(int, input().split(", "))
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split(", ")))
        current_matrix.append(row_data)

    return current_matrix


matrix = get_matrix()
sum_matrix = 0
for elem in matrix:
    sum_matrix += sum(elem)

print(sum_matrix)
print(matrix)


