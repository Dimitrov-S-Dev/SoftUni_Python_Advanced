from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches = 0
while males and females:
    curr_male = males[-1]
    curr_female = females[0]

    if curr_male <= 0:
        males.pop()
        continue

    if curr_female <= 0:
        females.popleft()
        continue

    if curr_male % 25 == 0:
        for index in range(2):
            if males:
                males.pop()
        continue

    if curr_female % 25 == 0:
        for index in range(2):
            if females:
                females.popleft()
        continue

    if curr_male == curr_female:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")
