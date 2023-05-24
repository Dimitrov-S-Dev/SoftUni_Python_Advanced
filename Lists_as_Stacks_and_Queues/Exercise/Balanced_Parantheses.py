from collections import deque

parentheses = deque(list(input()))
open_parentheses = deque()

while parentheses:
    left_parentheses = parentheses.popleft()

    if left_parentheses in "({[":
        open_parentheses.append(left_parentheses)

    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + left_parentheses}" not in "[]{}()":
            print("NO")
            break
else:
    print("YES")

# expression = input()
# opening_brackets = deque()

# pairs = {
#     "(": ")",
#     "{": "}",
#     "[": "]"
# }
# balanced = True
#
# for elem in expression:
#     if elem in "{[(":
#         opening_brackets.append(elem)
#     elif not opening_brackets:
#         balanced = False
#     else:
#         last_open_bracket = opening_brackets.pop()
#         if pairs[last_open_bracket] != elem:
#             balanced = False
#
#     if not balanced:
#         break
# if not balanced or opening_brackets:
#     print("NO")
# else:
#     print("YES")
#
