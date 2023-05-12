n = int(input())

matrix = [list(input()) for _ in range(n)]

sbl = input()
is_found = False

for row_index in range(n):
    if is_found:
        break
    for column_index in range(n):
        if matrix[row_index][column_index] == sbl:
            is_found = True
            print(f"({row_index}, {column_index})")
            break

if not is_found:
    print(f"{sbl} does not occur in the matrix")
