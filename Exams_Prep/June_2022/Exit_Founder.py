from collections import deque

players = deque(input().split(", "))
matrix = []

for _ in range(6):
    curr_row = input().split()
    matrix.append(curr_row)

rest = {
    "Tom": "No",
    "Jerry": "No",
}
while True:
    coordinates = list(input())
    row, col = int(coordinates[1]), int(coordinates[4])
    curr_player = players[0]

    if rest[curr_player] == "Yes":
        players.rotate(-1)
        rest[curr_player] = "No"
        continue

    if matrix[row][col] == "E":
        print(f"{curr_player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{curr_player} is out of the game! The winner is {players[1]}.")
        break

    elif matrix[row][col] == "W":
        print(f"{curr_player} hits a wall and needs to rest.")
        rest[curr_player] = "Yes"

    players.rotate(-1)
