from collections import deque
# read the input data
daily_portions = deque(int(x) for x in input().split(", "))
daily_stamina = deque(int(x) for x in input().split(", "))

# Initializing the Peaks and Difficulty

peaks = [
    {80: "Vihren"},
    {90: "Kutelo"},
    {100: "Banski Suhodol"},
    {60: "Polezhan"},
    {70: "Kamenitza"},

]

conquered_peaks = []
has_manage = False
index = 0

for day in range(7):
    curr_sum = daily_portions.pop() + daily_stamina.popleft()
    peak = peaks[index]
    for level, name in peak.items():
        if curr_sum >= level:
            conquered_peaks.append(name)
            if len(conquered_peaks) == 5:
                has_manage = True
                break
            index += 1

if has_manage:
    print("Alex did it! He climbed all top five Pirin peaks"
          " in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his "
          "journey better next time -> @PIRINWINS")
if conquered_peaks:
    print(f"Conquered peaks:")
    [print(x) for x in conquered_peaks]
