from collections import deque

# read the input data
food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
# Initializing the Peaks and Difficulty
peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
    }
conquered_peaks = []
failed_condition = False
day = 0
for key, value in peaks.items():
    while food and stamina:
        day += 1
        daily_sum = food.pop() + stamina.popleft()
        if daily_sum >= value and day <= 7:
            conquered_peaks.append(key)
            break
        if day >= 7:
            failed_condition = True
            break
    if failed_condition:
        break

if failed_condition:
    print(f"Alex failed! He has to organize his "
          "journey better next time -> @PIRINWINS")
else:
    print(f"Alex did it! He climbed all top five Pirin peaks "
          f"in one week -> @FIVEinAWEEK")

if conquered_peaks:
    print("Conquered peaks:")
    while conquered_peaks:
        print(conquered_peaks.pop(0))
