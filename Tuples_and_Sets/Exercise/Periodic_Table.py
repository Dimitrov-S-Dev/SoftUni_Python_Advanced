# elements = set()
# for _ in range(int(input())):
#     arg = input().split()
#     for a in arg:
#         elements.add("".join(a))
#
# print(*elements, sep="\n")

# elements = set()
#
# for _ in range(int(input())):
#     for elem in input().split():
#         elements.add(elem)
#
# print(*elements, sep="\n")

elements = []

for _ in range(int(input())):
    elements.extend(input().split())

print("\n".join(set(elements)))


