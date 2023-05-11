number_of_rows = int(input())
matrix = []

for _ in range(number_of_rows):
    curr_row = [int(x) for x in input().split(", ")]
    matrix.append(curr_row)

result = [num for row in matrix for num in row]
print(result)
