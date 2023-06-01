from module.Math import math_expression
first_num, operator, second_num = input().split()

print(f"{math_expression(float(first_num), operator, float(second_num)):.2f}")

