from collections import deque
# Task 1: Read the input data
times = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())

# Task 4: Initialize Ducks time

ranges = {
    (0, 61): "Darth Vader Ducky",
    (61, 121): "Thor Ducky",
    (121, 181): "Big Blue Rubber Ducky",
    (181, 241): "Small Yellow Rubber Ducky",
}

# Task 3: Initialize the variables
counts = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}
highest_range = 240

# Task 4 Main Loop
while times and tasks:
    condition = False
    curr_time = times.popleft()
    curr_task = tasks.pop()
    curr_count = curr_time * curr_task
    for start, end in ranges:
        if curr_count in range(start, end):
            curr_duck = ranges[start, end]
            counts[curr_duck] += 1
            condition = True
            break
    if not condition:
        if curr_count > highest_range:
            tasks.append(curr_task - 2)
            times.append(curr_time)

if not tasks:
    print("Congratulations, "
          "all tasks have been completed! Rubber ducks rewarded: ")
    for k, v in counts.items():
        print(f"{k}: {v}")



