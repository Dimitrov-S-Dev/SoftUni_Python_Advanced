longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [elem.split(",") for elem in input().split("-")]
    f_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    s_set = set(range(int(second_data[0]), int(second_data[1]) + 1))
    intersection = f_set.intersection(s_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is "
      f"[{', '.join(str(x) for x in longest_intersection)}]"
      f" with length {len(longest_intersection)}")
