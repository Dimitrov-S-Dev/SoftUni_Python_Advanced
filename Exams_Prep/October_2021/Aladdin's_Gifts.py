from collections import deque


def check_sum(presents_dict, number):
    element = None
    if 100 <= number <= 199:
        element = "Gemstone"
    elif 200 <= number <= 299:
        element = "Porcelain Sculpture"
    elif 300 <= number <= 399:
        element = "Gold"
    elif 400 <= number <= 499:
        element = "Diamond Jewellery"
    if element:
        presents_dict[element] += 1
    return presents_dict


materials = deque(int(x) for x in input().split())
magics = deque(int(x) for x in input().split())

presents = {
        "Gemstone": 0,
        "Porcelain Sculpture": 0,
        "Gold": 0,
        "Diamond Jewellery": 0,

    }

succeed = {
    1: [],
    2: [],
}

while materials and magics:
    curr_material = materials.pop()
    curr_magic = magics.popleft()
    curr_sum = curr_material + curr_magic

    if curr_sum < 100:
        if curr_sum % 2 == 0:
            curr_material *= 2
            curr_magic *= 3
            new_sum = curr_material + curr_magic
            presents = check_sum(presents, new_sum)
        else:
            new_sum = curr_sum * 2
            presents = check_sum(presents, new_sum)
    elif curr_sum > 499:
        curr_sum /= 2
        presents = check_sum(presents, curr_sum)

    else:
        presents = check_sum(presents, curr_sum)

is_succeed = False
if presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0:
    is_succeed = True
elif presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0:
    is_succeed = True

if is_succeed:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magics:
    print(f"Magic left: {', '.join(map(str, magics))}")

for k, v in sorted(presents.items()):
    if v > 0:
        print(f"{k}: {v}")
