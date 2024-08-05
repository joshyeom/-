# 전체 좌표를 훑으며 제일 큰 음식물을 찾기위해 BFS사용
# "."으로 매트릭스 생성
# 주어진 좌표를 "#"으로 변경
# 탐색 하면서 가장 큰 음식물을 최댓값으로 갱신

import sys
import collections
input = sys.stdin.readline
N, M, K = map(int, input().split())

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
matrix = [["." for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
max_value = 0


def bfs(start_x, start_y):
    visited[start_y][start_x] = True
    
    queue = collections.deque()
    queue.append((start_x, start_y))


    count = 1
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for dir in direction:
            new_x = curr_x + dir[0]
            new_y = curr_y + dir[1]

            if 0 <= new_x < M and 0 <= new_y < N and not visited[new_y][new_x] and matrix[new_y][new_x] == "#":
                count += 1
                queue.append((new_x, new_y))
                visited[new_y][new_x] = True

    return count


for _ in range(K):
    y, x = map(int, input().split())
    matrix[y - 1][x - 1] = "#"



for y in range(N):
    for x in range(M):
        if matrix[y][x] == "#" and not visited[y][x]:
            max_value = max(max_value, bfs(x, y))



print(max_value)