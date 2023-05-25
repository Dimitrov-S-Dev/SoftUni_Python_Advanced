from collections import deque

seats = deque(input().split(", "))
seats_1 = deque(int(x) for x in input().split(", "))
seats_2 = deque(int(x) for x in input().split(", "))

match_seats = 0
rotations = 0
seat_matches = []
while match_seats < 3 and rotations < 10:
    rotations += 1
    curr_seat_1 = seats_1.popleft()
    curr_seat_2 = seats_2.pop()
    sum_of_two = curr_seat_1 + curr_seat_2
    ascii_char = chr(sum_of_two)

    if f"{curr_seat_1}{ascii_char}" in seats:
        seats.remove(f"{curr_seat_1}{ascii_char}")
        match_seats += 1
        seat_matches.append(f"{curr_seat_1}{ascii_char}")

    elif f"{curr_seat_2}{ascii_char}" in seats:
        seats.remove(f"{curr_seat_2}{ascii_char}")
        match_seats += 1
        seat_matches.append(f"{curr_seat_2}{ascii_char}")
    else:
        seats_1.append(curr_seat_1)
        seats_2.appendleft(curr_seat_2)


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
