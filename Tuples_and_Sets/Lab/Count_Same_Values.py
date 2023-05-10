# values = tuple(map(float, input().split()))
# value_counter = {}
#
# for value in values:
#     if value not in value_counter:
#         value_counter[value] = 0
#     value_counter[value] += 1
#
# for k, v in value_counter.items():
#     print(f"{k} - {v} times")

numbers = [float(x) for x in input().split()]
numbers_dict = {x: numbers.count(x) for x in numbers}
for k, v in numbers_dict.items():
    print(f"{k} - {v} times")
