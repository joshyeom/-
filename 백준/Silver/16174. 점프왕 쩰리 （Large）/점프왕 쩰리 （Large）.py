import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)] 



def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True

    while queue:
        x, y = queue.popleft()
        value = matrix[y][x]

        # 오른쪽 이동
        nx = x + value
        if 0 <= nx < N and not visited[y][nx]:
            if matrix[y][nx] == -1:
                return True
            queue.append((nx, y))
            visited[y][nx] = True

        # 아래쪽 이동
        ny = y + value
        if 0 <= ny < N and not visited[ny][x]:
            if matrix[ny][x] == -1:
                return True
            queue.append((x, ny))
            visited[ny][x] = True

    return False

# BFS를 시작점 (0, 0)에서 시작
if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
