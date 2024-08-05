import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [ [False for _ in range(M * 3)] for _ in range(N)]
max_value = int(input())


def bfs(x, y):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()

    queue.append((x, y))
    visited[y][x] = True

    while queue:
        curr_x, curr_y = queue.popleft()
        for dir_x, dir_y in direction:
            new_x = curr_x + dir_x
            new_y = curr_y + dir_y

            if (0 <= new_x < (M * 3)
                and 0 <= new_y < N 
                and matrix[new_y][new_x] == 255
                and not visited[new_y][new_x]):
                    visited[new_y][new_x] = True
                    queue.append((new_x, new_y))

count = 0

for y in range(N):
    for x in range(0, M * 3, 3):  
        group = matrix[y][x:x + 3]
        avg = sum(group) / len(group) 
        if avg >= max_value:
            matrix[y][x:x + 3] = [255, 255, 255]
        else:
            matrix[y][x:x + 3] = [0, 0, 0]


for y in range(N):
    for x in range(M * 3):
        if not visited[y][x] and matrix[y][x] == 255:
            bfs(x, y)
            count += 1

print(count)