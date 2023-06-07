# Stage 1: Initialize the deque from input
from collections import deque

caffeine = deque(int(x) for x in input().split(", "))
drinks = deque(int(x) for x in input().split(", "))

# Stage 2: Initialize the variables
max_coffeine = 300
total_coffeine = 0

# Stage 3: Main Loop
while caffeine and drinks:
    curr_caffeine = caffeine.pop()
    curr_drink = drinks.popleft()
    curr_result = curr_caffeine * curr_drink

    if curr_result <= max_coffeine:
        total_coffeine += curr_result
        max_coffeine -= curr_result
    else:
        drinks.append(curr_drink)

        if total_coffeine >= 30:
            total_coffeine -= 30
            max_coffeine += 30
        else:
            total_coffeine = 0
            max_coffeine = 300

# Stage 4: Print Output

if drinks:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_coffeine} mg caffeine.")
