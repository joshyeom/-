import sys
sys.setrecursionlimit(10000)
from sys import stdin
input = stdin.readline

def dfs(w, h, x, y, matrix):
    directions = [[0, 1], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, -1], [-1, 0]]

    for dir_ in directions:
        new_x = x + dir_[0]
        new_y = y + dir_[1]

        if 0 <= new_x < w and 0 <= new_y < h and matrix[new_y][new_x] == "1":
            matrix[new_y][new_x] = "."
            dfs(w, h, new_x, new_y, matrix)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    matrix = [input().strip().split() for _ in range(h)]

    count = 0

    for y in range(h):
        for x in range(w):
            if matrix[y][x] == "1":
                matrix[y][x] = "."
                dfs(w, h, x, y, matrix)
                count += 1

    print(count)
