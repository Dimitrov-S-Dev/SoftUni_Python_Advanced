# Stage 1: Initialize seats and deque from input
from collections import deque

seats = input().split(", ")
nums1 = deque(int(x) for x in input().split(", "))
nums2 = deque(int(x) for x in input().split(", "))

# Stage 2: Initialize variables
seat_matches = 0
rotations = 0
matched_seats = []

while seat_matches < 3 and rotations < 10:
    first_num = nums1.popleft()
    second_num = nums2.pop()
    current_sum = first_num + second_num
    current_char = chr(current_sum)
    curr_seats = [f"{first_num}{current_char}", f"{second_num}{current_char}"]

    for element in curr_seats:
        if element in seats:
            index = seats.index(element)
            removed = seats.pop(index)
            matched_seats.append(removed)
            seat_matches += 1
            continue
        elif element in matched_seats:
            continue
    nums1.append(first_num)
    nums2.appendleft(second_num)
    rotations += 1

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
