import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline
h, w = map(int, input().split())

matrix = [input().split() for _ in range(h)]

picture = 0
biggest = 0

def dfs(w, h, x, y, matrix):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    matrix[y][x] = "."
    size = 1

    for dir_ in directions:
        new_x = x + dir_[0]
        new_y = y + dir_[1]

        if 0 <= new_x < w and 0 <= new_y < h and matrix[new_y][new_x] == "1":
            size += dfs(w, h, new_x, new_y, matrix)
        
    return size


for y in range(h):
    for x in range(w):
        if matrix[y][x] == "1":
            new_size = dfs(w, h, x, y, matrix)
            biggest = max(biggest, new_size )
            picture += 1

print(picture)
print(biggest)
