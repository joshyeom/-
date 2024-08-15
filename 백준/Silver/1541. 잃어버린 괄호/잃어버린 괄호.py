import sys
input = sys.stdin.readline
M = input().strip().split("-")

nums = []

for exp in M:
    nums.append(sum(map(int, exp.split("+"))))

minus = []

for num in range(len(M) - 1):
    minus.append(nums.pop())

print(sum(nums) - sum(minus))

