def print_line(nums):
    print(*[num for num in range(1, nums + 1)], sep=" ")


def print_triangle(size):
    for row in range(1, size + 1):
        print_line(row)

    for row in range(size - 1, 0, -1):
        print_line(row)
