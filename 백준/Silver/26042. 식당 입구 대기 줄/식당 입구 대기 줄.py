from sys import stdin
input = stdin.readline
from collections import deque
N = int(input())


arr = deque()
answer = [0, 0]

for _ in range(N):
    info = list(map(int, input().strip().split()))
    
    if info[0] == 1:
        arr.append(info[1])
    else:
        arr.popleft()

    if answer[0] < len(arr):
        answer[0] = len(arr)
        answer[1] = arr[-1]
    elif answer[0] == len(arr):
        answer[1] = min(answer[1], arr[-1])

print(" ".join(map(str, answer)))