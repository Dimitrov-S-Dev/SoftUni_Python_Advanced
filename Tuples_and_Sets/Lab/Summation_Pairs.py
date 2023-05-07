import itertools

numbers = [int(x) for x in input().split()]
target = int(input())

result = set([x for x in itertools.combinations(numbers, r=2) if x[0] + x[1] == target])

for res in result:
    print(f"{res[0]} + {res[1]} = {target}")

