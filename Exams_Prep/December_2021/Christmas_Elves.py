from collections import deque

elfs = deque(int(x) for x in input().split())
boxes = deque(int(x) for x in input().split())

times = 0
used_energy = 0
toys = 0

while elfs and boxes:
    elf = elfs[0]
    box = boxes[-1]

    if elf < 5:
        elfs.popleft()
        continue

    times += 1

    if times % 15 == 0 or times % 3 == 0:
        box *= 2

    if elf < box:
        elfs.rotate(- 1)
        elfs[- 1] *= 2
        continue

    curr_used_energy = elf - box
    if times % 5 != 0:
        curr_used_energy += 1

    if times % 3 == 0 and times % 5 != 0:
        toys += 2

    elif times % 5 != 0:
        toys += 1

    boxes.pop()
    elfs.popleft()
    elfs.append(curr_used_energy)
    used_energy += box

print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elfs:
    print(f"Elves left: {', '.join(str(x) for x in elfs)}")
if boxes:
    print(f"Boxes left: {', '.join(str(x) for x in boxes)}")
