from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
numbers = sorted(map(int, input().split()))

answer = 0
active = 0

for el in numbers:
    answer += el * active

    if active < k:
        active += 1

print(answer)