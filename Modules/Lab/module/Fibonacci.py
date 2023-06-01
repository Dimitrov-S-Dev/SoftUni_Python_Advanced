def create(n):
    if n == 1:
        return [0]
    if n == 0:
        return []
    result = [0, 1]
    for _ in range(n - 2):
        result.append(result[-1] + result[-2])
    return result


def locate(target, nums):
    try:
        return nums.index(target)
    except IndexError:
        return False


def parse_line(line):
    args = line.split()
    return ("Create", int(args[2]) if args[0] == "Create" else ("Locate", int(args[1])))

