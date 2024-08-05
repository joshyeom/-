from sys import stdin
from collections import deque
input = stdin.readline
N, M = map(int, input().split())

matrix = [input().strip() for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False for _ in range(M)] for _ in range(N)]

queue = deque()

for x in range(M):
    if matrix[0][x] == "0":
        queue.append((0, x))
        visited[0][x] = True

while queue:
    current_y, current_x = queue.popleft()

    if current_y == N - 1:
        print("YES")
        exit()

    for dir in direction:
        dir_x, dir_y = dir
        new_x = dir_x + current_x
        new_y = dir_y + current_y

        if 0 <= new_x < M and 0 <= new_y < N:
                if not visited[new_y][new_x] and matrix[new_y][new_x] == "0":
                    visited[new_y][new_x] = True
                    queue.append((new_y, new_x))

print("NO")