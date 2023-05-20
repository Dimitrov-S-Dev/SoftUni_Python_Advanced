def solve_shooting_range():
    # Read the field
    field = []
    for _ in range(5):
        row = input().split()
        field.append(row)

    # Initialize variables
    targets = []
    target_count = 0
    current_position = (0, 0)
    targets_removed = []
    # Find initial position and targets
    for i in range(5):
        for j in range(5):
            if field[i][j] == 'A':
                current_position = (i, j)
            elif field[i][j] == 'x':
                targets.append((i, j))
                target_count += 1

    # Number of commands
    num_commands = int(input())

    # Define directions
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    # Process commands
    for _ in range(num_commands):
        if not target_count:
            break
        command, *data = input().split()
        action = command
        direction = data[0]

        # Move action
        if action == 'move':
            dx, dy = directions[direction]
            x, y = current_position

            steps = int(data[1])
            for _ in range(steps):
                x += dx
                y += dy

            if x in range(5) and y in range(5) and field[x][y] == '.':
                current_position = (x, y)

        # Shoot action
        elif action == 'shoot':
            x, y = current_position
            dx, dy = directions[direction]

            while True:
                x += dx
                y += dy

                if x not in range(5) or y not in range(5):
                    break

                if field[x][y] != "x":
                    continue

                if field[x][y] == 'x':
                    targets_removed.append([x, y])
                    targets.remove((x, y))
                    field[x][y] = '.'
                    target_count -= 1
                    break

    # Check if all targets were hit
    if target_count == 0:
        print(f"Training completed! All {len(targets_removed)} targets hit.")
    else:
        print(f"Training not completed! {target_count} targets left.")

    # Print the index positions of hit targets
    for target in targets_removed:
        print(target)


solve_shooting_range()
