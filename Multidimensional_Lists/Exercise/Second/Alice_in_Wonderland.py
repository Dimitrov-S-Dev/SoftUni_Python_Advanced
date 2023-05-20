def move_alice(matrix, row, col, direction):
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return row, col


def is_valid_move(matrix, row, col):
    n = len(matrix)
    if row not in range(len(matrix)) or col not in range(len(matrix)):
        return False
    return True


def alice_tea_party():
    n = int(input())
    matrix = []
    alice_row = alice_col = 0

    for row in range(n):
        row_data = input().split()
        if "A" in row_data:
            alice_row = row
            alice_col = row_data.index("A")
            row_data[alice_col] = "*"
        matrix.append(row_data)

    collected_tea = 0
    while collected_tea < 10:
        curr_move = input()
        new_row, new_col = move_alice(matrix, alice_row, alice_col, curr_move)
        if not is_valid_move(matrix, new_row, new_col):
            break

        if matrix[new_row][new_col] == "R":
            matrix[new_row][new_col] = "*"
            break

        if matrix[new_row][new_col].isdigit():
            collected_tea += int(matrix[new_row][new_col])

        matrix[new_row][new_col] = "*"
        alice_row, alice_col = new_row, new_col

    if collected_tea >= 10:
        print("She did it! She went to the party.")
    else:
        print("Alice didn't make it to the tea party.")

    for row in matrix:
        print(" ".join(row))


alice_tea_party()
