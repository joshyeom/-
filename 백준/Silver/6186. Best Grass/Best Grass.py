# range 설정을 잘못해서 계속 실패
# 맵을 순회하다가 #을 만나면 인근 #으로 옮겨감
# DFS


from sys import stdin
input = stdin.readline

lines, row = map(int, input().split())
map = [input().strip() for _ in range(lines)]

visited = []
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

count = 0

def solution(x, y):
    if [x, y] in visited:
        return
    
    visited.append([x, y])

    for i in range(len(dir)):
        new_x = x + dir[i][0]
        new_y = y + dir[i][1]

        if 0 <= new_x < lines and 0 <= new_y < row:
            if map[new_x][new_y] == "#":
                solution(new_x, new_y)


for x in range(lines):
    for y in range(row):
        if map[x][y] == "#" and [x, y] not in visited:
            solution(x, y)
            count += 1

print(count)
