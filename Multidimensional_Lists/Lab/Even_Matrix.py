number_of_rows = int(input())

matrix = []

for _ in range(number_of_rows):
    curr_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(curr_row)

print(matrix)
