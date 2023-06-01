from module.Fibonacci import create, locate, parse_line

nums = []
while True:
    command = input()
    if command == "Stop":
        break
    sub_comm, num = parse_line(command)
    if sub_comm == "Create":
        nums = create(num)
        print(nums)
    else:
        index = locate(num, nums)
        output = f"The number {num} is not in sequence" if not index else \
            f"The number - {num} is at index {index}"
        print(output)

