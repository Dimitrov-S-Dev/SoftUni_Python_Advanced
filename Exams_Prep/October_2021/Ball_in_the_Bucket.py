size = 6
matrix = []

for _ in range(size):
    curr_row = input().split()
    matrix.append(curr_row)

points = 0
hit_place = []

for _ in range(3):
    curr_row, curr_col = [int(x) for x in input().strip("()").split(", ")]

    if curr_row not in range(6) or curr_col not in range(6):
        continue
    if matrix[curr_row][curr_col] == "B":
        if [curr_row, curr_col] not in hit_place:
            hit_place.append([curr_row, curr_col])
            for index in range(6):
                if matrix[index][curr_col].isdigit():
                    points += int(matrix[index][curr_col])


prize = None
if points in range(100, 200):
    prize = "Football"
elif points in range(200, 300):
    prize = "Teddy Bear"
elif points >= 300:
    prize = "Lego Construction Set"

if points >= 100:
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    diff = 100 - points
    print(f"Sorry! You need {diff} points more to win a prize.")
