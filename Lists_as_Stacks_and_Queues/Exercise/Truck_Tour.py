from collections import deque


# pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
#
# pumps_data_copy = pumps_data.copy()
# index = 0
# gas_in_tank = 0
#
# while pumps_data_copy:
#     petrol, distance = pumps_data_copy.popleft()
#
#     gas_in_tank += petrol
#     if gas_in_tank - distance < 0:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#         index += 1
#         gas_in_tank = 0
#     else:
#         gas_in_tank -= distance
#
# print(index)
pumps_count = int(input())
pumps = deque([int(x) for x in input().split()]for _ in range(pumps_count))

for attempt in range(pumps_count):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk += petrol + trunk - distance

        if trunk < 0:
            flag = True
            break
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
