# def get_add(seq, args):
#     for num in args:
#         seq.add(num)
#     return seq
#
#
# def get_remove(seq, args):
#     for num in args:
#         if num in seq:
#             seq.remove(int(num))
#     return seq
#
#
# def get_check(seq_1, seq_2):
#     if seq_1.issubset(seq_2) or seq_2.issubset(seq_1):
#         print("True")
#     else:
#         print("False")
#
#
# def get_numbers(first, second, count_iter):
#     for _ in range(count_iter):
#         command, sequence, *args = input().split()
#         nums = [int(x) for x in args]
#         if command == "Add":
#             if sequence == "First":
#                 first = get_add(first, nums)
#             elif sequence == "Second":
#                 second = get_add(second, nums)
#
#         elif command == "Remove":
#             if sequence == "First":
#                 first = get_remove(first, nums)
#             elif sequence == "Second":
#                 second = get_remove(second, nums)
#
#         elif command == "Check":
#             get_check(first, second)
#
#     print(*first, sep=", ")
#     print(*second, sep=", ")
#
#
# nums_one = set([int(x) for x in input().split()])
# nums_two = set([int(x) for x in input().split()])
# n = int(input())
# get_numbers(nums_one, nums_two, n)


# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)
#
#     if command == "Add First":
#         [first.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first.remove(int(el)) for el in data if int(el) in first]
#     elif command == "Remove Second":
#         [second.discard(int(el)) for el in data]
#     else:
#         if first.issubset(second) or second.issubset(first):
#             print("True")
#         else:
#             print("False")
#
# print(*first, sep=", ")
# print(*second, sep=", ")


first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first.add(int(el)) for el in x],
    "Add Second": lambda x: [second.add(int(el)) for el in x],
    "Remove First": lambda x: [first.remove(int(el)) for el in x if int(el) in first],
    "Remove Second": lambda x: [second.discard(int(el)) for el in x],
    "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)
}
for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + " " + data.pop(0)

    if data:
        functions[command](data)
    else:
        functions[command]()

print(*first, sep=", ")
print(*second, sep=", ")
