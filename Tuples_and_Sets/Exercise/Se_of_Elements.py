n, m = [int(x) for x in input().split()]

set_n = set()
set_m = set()

for _ in range(n):
    number = int(input())
    set_n.add(number)

for _ in range(m):
    number = int(input())
    set_m.add(number)

result = set_n.intersection(set_m)

for res in result:
    print(res)
