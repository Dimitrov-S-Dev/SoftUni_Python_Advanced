from collections import deque

# read the input data
food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
# Initializing the Peaks and Difficulty
peaks = deque([
    ["Vihren", 80],
    ["Kutelo", 90],
    ["Banski Suhodol", 100],
    ["Polezhan", 60],
    ["Kamenitza", 70],
])
conquered_peaks = []
failed_condition = False
day = 1

while True:
    if len(conquered_peaks) == 5:
        print(f"Alex did it! He climbed all top five Pirin peaks "
              f"in one week -> @FIVEinAWEEK")
        break
    if not food or day > 7:
        print(f"Alex failed! He has to organize his "
              "journey better next time -> @PIRINWINS")
        break

    daily_sum = food.pop() + stamina.popleft()
    name, value = peaks.popleft()
    if daily_sum >= value:
        conquered_peaks.append(name)
    else:
        peaks.appendleft([name, value])
    day += 1

if conquered_peaks:
    print("Conquered peaks:")
    [print(x) for x in conquered_peaks]
