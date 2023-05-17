# from collections import deque
#
# words = deque(input().split())
# colors = {"red", "yellow", "blue", "orange", "purple", "green"}
# req_colors = {
#     "orange": {"red", "yellow"},
#     "purple": {"red", "blue"},
#     "green": {"yellow", "blue"},
# }
# result = []
#
# while words:
#     first_word = words.popleft()
#     second_word = words.pop() if words else ""
#
#     for color in (first_word + second_word, second_word + first_word):
#         if color in colors:
#             result.append(color)
#             break
#     else:
#         for el in (first_word[: -1], second_word[: -1]):
#             if el:
#                 words.insert(len(words) // 2, el)
#
# for color in set(req_colors.keys()).intersection(result):
#     if not req_colors[color].issubset(result):
#         result.remove(color)
#
# print(result)

from collections import deque

words = deque(input().split())
primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

while words:
    left = words.popleft()
    right = words.pop() if words else ""

    result = left + right
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = right + left
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, result)
    if right:
        words.insert(len(words) // 2, result)


