# from functools import reduce
#
#
# expression = input().split()
#
# index = 0
#
# functions = {
#     "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
#     "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
#     "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
#     "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
# }
#
# while index < len(expression):
#     element = expression[index]
#
#     if element in "*/+-":
#         result = functions[element](index)
#         [expression.pop(1) for i in range(index)]
#         expression[0] = result
#         index = 0
#     index += 1
#
# print(int(expression[0]))

from collections import deque

expression = deque(input().split())

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element == "*":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))

    elif element == "+":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    elif element == "-":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))

    elif element == "/":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))

    if element in "+-*/":
        del expression[1]
        idx = 0

    idx += 1


print(int(expression[0]))
