def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for i in range(2, n):
        row = [1]

        for j in range(1, i):

            num = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(num)

        row.append(1)
        triangle.append(row)

    return triangle

print(get_magic_triangle(5))


