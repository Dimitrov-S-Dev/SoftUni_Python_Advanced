# Initialize a function to check the position
from collections import deque


def get_position_check(matrix, row, col):
    if matrix[row][col] == "E":
        return "win"
    elif matrix[row][col] == "T":
        return "lose"
    elif matrix[row][col] == "W":
        return "rest"


# Initialize matrix 6 x 6 and players
players = deque(input().split(", "))
matrix = []

for _ in range(6):
    row_data = input().split()
    matrix.append(row_data)

# Main Loop

turn_count = 0
even_rest = False
odd_rest = False
while True:
    turn_count += 1
    curr_row, curr_col = [int(x) for x in input().strip("()").split(", ")]

    if turn_count % 2 != 0:
        if odd_rest:
            odd_rest = False
            players.rotate(-1)
            continue
    else:
        if even_rest:
            even_rest = False
            players.rotate(- 1)
            continue

    player = players.popleft()

    result = get_position_check(matrix, curr_row, curr_col)

    if result == "win":
        print(f"{player} found the Exit and wins the game!")
        break

    elif result == "lose":
        print(f"{player} is out of the game! The winner is {players.pop()}.")
        break

    elif result == "rest":
        print(f"{player} hits a wall and needs to rest.")
        if turn_count % 2 != 0:
            odd_rest = True
        else:
            even_rest = True

    players.append(player)
