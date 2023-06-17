from collections import deque
# Task 1 Initialize the deque from input data

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = [int(x) for x in input().split()]

# Task 2 Loop over the collections
while tools and substances:
    curr_tool = tools[0]
    curr_substance = substances[-1]
    curr_multiply = curr_tool * curr_substance

    if curr_multiply in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(curr_multiply)

    else:

        tools.append(tools.popleft() + 1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()


if (len(tools) == 0 or len(substances) == 0) and len(challenges) > 0:
    print("Harry is lost in the temple. Oblivion awaits him.")

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")