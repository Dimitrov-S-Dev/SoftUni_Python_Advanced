def get_add(seq, args):
    for num in args:
        seq.add(num)
    return seq


def get_remove(seq, args):
    for num in args:
        if num in seq:
            seq.remove(int(num))
    return seq


def get_check(seq_1, seq_2):
    if seq_1.issubset(seq_2) or seq_2.issubset(seq_1):
        print("True")
    else:
        print("False")


def get_numbers(first, second, count_iter):
    for _ in range(count_iter):
        command, sequence, *args = input().split()
        nums = [int(x) for x in args]
        if command == "Add":
            if sequence == "First":
                first = get_add(first, nums)
            elif sequence == "Second":
                second = get_add(second, nums)

        elif command == "Remove":
            if sequence == "First":
                first = get_remove(first, nums)
            elif sequence == "Second":
                second = get_remove(second, nums)

        elif command == "Check":
            get_check(first, second)

    print(*first, sep=", ")
    print(*second, sep=", ")


nums_one = set([int(x) for x in input().split()])
nums_two = set([int(x) for x in input().split()])
n = int(input())
get_numbers(nums_one, nums_two, n)


