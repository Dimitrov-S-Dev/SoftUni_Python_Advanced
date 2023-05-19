elements = input().split("|")
result = []
for index in range(len(elements) - 1, -1, -1):
    curr_element = elements[index].strip().split()
    result.extend(curr_element)
print(" ".join(result))


