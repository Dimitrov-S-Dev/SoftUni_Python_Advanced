from collections import deque

# Step 1: Read input
elf_energy = deque(map(int, input().split()))
materials = deque(map(int, input().split()))

# Step 2: Initialize variables
total_energy_used = 0
total_toys_made = 0
counter = 0

# Step 3: Main loop
while elf_energy and materials:
    # Step 5: Check if elf has enough energy
    elf = elf_energy[0]
    if elf < 5:
        elf_energy.popleft()
        continue

    counter += 1
    # Step 4: Check if elf can make a toy
    if materials[-1] > elf_energy[0]:
        current_elf = elf_energy.popleft()
        elf_energy.append(current_elf * 2)
        continue

    # Step 6: Calculate required energy and make a toy
    energy = elf_energy.popleft()
    material = materials.pop()

    used_energy = 0
    left_energy = 0
    current_toys = 0

    if counter % 15 == 0:
        if material * 2 <= energy:
            used_energy = material * 2
            left_energy = energy - material * 2
        else:
            left_energy = energy * 2
            materials.append(material)

    elif counter % 5 == 0:
        used_energy = material
        left_energy = energy - used_energy

    elif counter % 3 == 0:
        if material * 2 <= energy:
            used_energy = material * 2
            left_energy = (energy - material * 2) + 1
            current_toys += 2
        else:
            left_energy = energy * 2
            materials.append(material)
    else:
        current_toys += 1
        used_energy = material
        left_energy = (energy - used_energy) + 1

    total_energy_used += used_energy
    total_toys_made += current_toys
    elf_energy.append(left_energy)

# Step 7: Print results
print(f"Toys made: {total_toys_made}")
print(f"Total energy used: {total_energy_used}")
if elf_energy:
    print(f"Elves left: {' '.join(map(str, elf_energy))}")
else:
    print(f"Boxes left: {' '.join(map(str, materials))}")
