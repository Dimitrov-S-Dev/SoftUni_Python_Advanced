number_of_rows = int(input())
result = []

for _ in range(number_of_rows):
    [result.append(int(x)) for x in input().split(", ")]

print(result)