# 좌표를 탐색하면서 ".", "v", "o"를 만나면 BFS 탐색 시작
# "#"로 사방이 막힐때까지 BFS탐색
# "v", "o"를 만날때마다 개수를 세기
# "v"가 "o"와 같거나 크다면 = "v"
# "o"가 더 많다면 = "o"

import sys
import collections
input = sys.stdin.readline
col, row = map(int, input().split())

matrix = [input().strip() for _ in range(col)]
visited = [[False for _ in range(row)] for _ in range(col)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

total_wolf = 0
total_sheep = 0

def bfs(start_y, start_x):
    queue = collections.deque()

    wolf = 0
    sheep = 0

    if matrix[start_y][start_x] == "v":
        wolf += 1
    elif matrix[start_y][start_x] == "o":
        sheep += 1

    visited[start_y][start_x] = True
    queue.append((start_y, start_x))

    while queue:
        curr_y, curr_x = queue.popleft()
        
        for dir in direction:
            move_y, move_x = dir
            new_y = curr_y + move_y
            new_x = curr_x + move_x

            if 0 <= new_y < col and 0 <= new_x < row and matrix[new_y][new_x] != "#" and not visited[new_y][new_x]:
                queue.append((new_y, new_x))
                visited[new_y][new_x] = True

                if matrix[new_y][new_x] == "v":
                    wolf += 1
                elif matrix[new_y][new_x] == "o":
                    sheep += 1
    
    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    
    return (sheep, wolf)


for y in range(col):
    for x in range(row):
        if matrix[y][x] != "#" and not visited[y][x]:
            sheep, wolf = bfs(y, x)
            total_wolf += wolf
            total_sheep += sheep

print(total_sheep, total_wolf)