from collections import deque

effects = deque(int(x) for x in input().split(", "))
powers = deque(int(x) for x in input().split(", "))

fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0,

}

fireworks_list = [
    "Palm", "Palm", "Palm",
    "Willow", "Willow", "Willow",
    "Crossette", "Crossette", "Crossette"

]

while effects and powers:
    effect = effects.popleft()
    power = powers.pop()
    if effect <= 0 and power <= 0:
        continue
    elif effect <= 0:
        powers.append(power)
        continue
    elif power <= 0:
        effects.appendleft(effect)
        continue

    curr_sum = effect + power
    firework = None

    if curr_sum % 3 == 0 and curr_sum % 5 != 0:
        fireworks["Palm"] += 1
        firework = "Palm"

    elif curr_sum % 5 == 0 and curr_sum % 3 != 0:
        fireworks["Willow"] += 1
        firework = "Willow"

    elif curr_sum % 3 == 0 and curr_sum % 5 == 0:
        fireworks["Crossette"] += 1
        firework = "Crossette"

    else:
        effects.append(effect - 1)
        powers.append(power)

    if firework in fireworks_list:
        fireworks_list.remove(firework)
        if not fireworks_list:
            break

if not fireworks_list:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in powers)}")

for k, v in fireworks.items():
    print(f"{k} Fireworks: {v}")
