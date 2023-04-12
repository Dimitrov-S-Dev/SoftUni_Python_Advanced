from collections import deque

liters = int(input())
line = deque()

while True:
    command = input()
    if command == "Start":
        break
    line.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if liters >= required_liters:
            liters -= required_liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    else:
        _, liters_to_fill = command.split()
        liters += int(liters_to_fill)

print(f"{liters} liters left")
