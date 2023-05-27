from collections import deque

# Stage 1: Initialize the dequeue from input data
effects = deque(int(x) for x in input().split(", "))
casings = deque(int(x) for x in input().split(", "))

# Stage 2: Initialize materials

materials = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",
}

# Stage 4: Main Loop and variables initialization
bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}
# When to stop the Loop  when all have 3 counts
bombs_list = [
    "Datura Bombs", "Datura Bombs", "Datura Bombs",
    "Cherry Bombs", "Cherry Bombs", "Cherry Bombs",
    "Smoke Decoy Bombs", "Smoke Decoy Bombs", "Smoke Decoy Bombs",
]
while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    curr_sum = effect + casing

    if curr_sum in materials.keys():
        bomb = materials[curr_sum]
        bombs[bomb] += 1
        if bomb in bombs_list:
            bombs_list.remove(bomb)
            if not bombs_list:
                break

    else:
        effects.appendleft(effect)
        casings.append(casing - 5)

# Stage 5: find out the print output
is_succeeded = True
for v in bombs.values():
    if v < 3:
        is_succeeded = False
        break

# Stage 6: Print

if is_succeeded:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in effects)}")
else:
    print(f"Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
else:
    print(f"Bomb Casings: empty")

for k, v in sorted(bombs.items()):
    print(f"{k}: {v}")
