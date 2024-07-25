from sys import stdin
input = stdin.readline
from collections import deque
n = int(input())

for i in range(1, n + 1):
    N, M = map(int, input().split())
    docs = deque(list(map(int, input().split())))
    count = 0
    current_index = M

    while len(docs) > 0:
        maximum = max(docs)
        first = docs.popleft()
        current_index -= 1 

        if first == maximum:
            count += 1
            if current_index < 0:
                print(count)
                break

        else:
            docs.append(first)
            if current_index < 0:
                current_index = len(docs) -1
