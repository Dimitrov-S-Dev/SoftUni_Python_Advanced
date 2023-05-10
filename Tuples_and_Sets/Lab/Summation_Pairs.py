# import itertools
#
# numbers = [int(x) for x in input().split()]
# target = int(input())
#
# result = set([x for x in itertools.combinations(numbers, r=2) if x[0] + x[1] == target])
#
# for res in result:
#     print(f"{res[0]} + {res[1]} = {target}")

numbers = [1, 3, 2, 4, 5, -2, -1, 5, 3, -3, 7, 0]

target = 4
values_map = {}
targets = set()

for value in numbers:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f"{p1} + {p2} = {target}")
    else:
        targets.add(target - value)
        values_map[target - value] = value
