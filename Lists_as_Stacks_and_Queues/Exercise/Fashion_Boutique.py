# clothes = [int(n) for n in input().split()]
# rack_space = int(input())
#
# rack_count = 1
# current_rack_space = rack_space
#
# while clothes:
#     cloth = clothes.pop()
#
#     if current_rack_space - cloth >= 0:
#         current_rack_space -= cloth
#     else:
#         rack_count += 1
#         current_rack_space = rack_space - cloth
# print(rack_count)

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

curr_rack_capacity = rack_capacity
rack_count = 0

while clothes:
    cloth = clothes[-1]

    if cloth > curr_rack_capacity:
        rack_count += 1
        curr_rack_capacity = rack_capacity
    else:
        curr_rack_capacity -= cloth
        clothes.pop()

print(rack_count)
