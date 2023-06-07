# Step 1: Initialize the food and stamina from input
from collections import deque

food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))


# Step 2: Create peaks with difficulty level

peaks = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza",

}

# Step 3: Initialize the output variables

conquered_peaks = []

# Step 4: Main Loop

for level in peaks.keys():
    while food:
        curr_food = food.pop()
        curr_stamina = stamina.popleft()
        curr_sum = curr_food + curr_stamina
        if curr_sum >= level:
            conquered_peaks.append(peaks[level])
            break
        else:
            continue

if len(conquered_peaks) == len(peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> "
          "@FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> "
          "@PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for conquered in conquered_peaks:
        print(conquered)