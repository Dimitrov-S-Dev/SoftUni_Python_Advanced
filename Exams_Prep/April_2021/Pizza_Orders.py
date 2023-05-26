from collections import deque
# Stage 1: Initialize deque inputs
orders = deque(int(x) for x in input().split(", "))
employees = deque(int(x) for x in input().split(", "))

# Stage 2: Create variables
total_pizzas = 0

# Stage 3: Main Loop

while orders and employees:
    if orders[0] <= 0 or orders[0] > 10:
        orders.popleft()
        continue

    order = orders.popleft()
    employee = employees.pop()

    if employee >= order:
        total_pizzas += order

    else:
        remaining = order - employee
        total_pizzas += employee
        orders.appendleft(remaining)


if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
