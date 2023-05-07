n = int(input())
usernames = set()

for _ in range(n):
    username = input()
    usernames.add(username)

print(*usernames,sep="\n")

print(*{input() for _ in range(int(input()))},sep="\n")
