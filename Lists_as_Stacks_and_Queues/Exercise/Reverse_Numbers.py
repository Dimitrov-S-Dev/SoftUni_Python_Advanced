# nums = input().split()
#
# while nums:
#     print(nums.pop(), end=" ")

print(*input().split()[:: -1], sep=" ")
