from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))

BOX = 50
box_count = 0
bad_luck = 0
while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        switch = papers.pop()
        papers.rotate(-1)
        papers.appendleft(switch)

        continue
    paper = papers.pop()
    sum_ = egg + paper

    if sum_ <= 50:
        box_count += 1

if box_count >= 1:
    print(f"Great! You filled {box_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
