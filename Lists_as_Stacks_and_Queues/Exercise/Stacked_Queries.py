from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)),
    4: lambda x: print(min(numbers))
}
for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)

numbers.reverse()
print(*numbers, sep=", ")
