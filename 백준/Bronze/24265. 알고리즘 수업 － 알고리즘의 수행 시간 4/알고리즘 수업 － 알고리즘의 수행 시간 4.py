import sys
input = sys.stdin.readline

n = int(input())

# 등차 수열의 합
# https://mathbang.net/609#gsc.tab=0
print(int(n * (n - 1) - (n - 1) * n / 2))

# [6, 5, 4, 3, 2, 1]

print(2)