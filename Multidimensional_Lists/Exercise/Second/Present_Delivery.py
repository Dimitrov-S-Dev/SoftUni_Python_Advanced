def get_present_delivery():
    # Read the presents count and create the matrix
    presents = int(input())
    size = int(input())
    nb_hood = []

    for _ in range(size):
        row_data = input().split()
        nb_hood.append(row_data)

    # Get the current position
    current_position = (0, 0)
    happy_kids = 0
    for row in range(size):
        for col in range(size):
            if nb_hood[row][col] == "S":
                current_position = (row, col)
            elif nb_hood[row][col] == "V":
                happy_kids += 1
    nice_kids = happy_kids
    #  Initializes Directions
    directions = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1),
    }

    # Read the commands
    while presents:
        command = input()
        if command == "Christmas morning":
            break

        dr, dc = directions[command]
        x, y = current_position
        nb_hood[x][y] = "-"
        x += dr
        y += dc

        # Get the cell value
        # V - nice kid
        # X - naughty kid
        # C - cookie
        if x in range(size) and y in range(size):
            current_position = (x, y)
            if nb_hood[x][y] == "V":
                nb_hood[x][y] = "S"
                if presents:
                    presents -= 1
                    happy_kids -= 1

            elif nb_hood[x][y] == "C":
                nb_hood[x][y] = "S"
                for direction in directions.keys():
                    dr, dc = directions[direction]
                    x, y = current_position
                    x += dr
                    y += dc
                    if nb_hood[x][y] == "X":
                        if presents:
                            presents -= 1
                            nb_hood[x][y] = "-"
                        else:
                            break

                    elif nb_hood[x][y] == "V":
                        if presents:
                            presents -= 1
                            happy_kids -= 1
                            nb_hood[x][y] = "-"
                        else:
                            break

    # Print the result
    if not presents:
        if happy_kids > 0:
            print("Santa ran out of presents!")
    [print(*row) for row in nb_hood]

    if happy_kids:
        print(f"No presents for {happy_kids} nice kid/s.")
    else:
        print(f"Good job, Santa! {nice_kids} happy nice kid/s.")


get_present_delivery()
