values = tuple(map(float, input().split()))
value_counter = {}

for value in values:
    if value not in value_counter:
        value_counter[value] = 0
    value_counter[value] += 1

for k, v in value_counter.items():
    print(f"{k} - {v} times")
