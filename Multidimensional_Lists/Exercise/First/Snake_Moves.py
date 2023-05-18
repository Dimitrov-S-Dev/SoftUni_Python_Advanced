rows, columns = [int(x) for x in input().split()]
word = input()
index = 0

for row in range(rows):
    element = [None] * columns
    if row % 2 == 0:
        for col in range(columns):
            element[col] = word[index % len(word)]
            index += 1
    else:
        for col in range(columns - 1, -1, -1):
            element[col] = word[index % len(word)]
            index += 1
    print("".join(element))
