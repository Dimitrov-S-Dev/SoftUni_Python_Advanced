def print_triangle(size):
    for row in range(1, size + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()

    for row in range(size - 1, 0, -1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()

