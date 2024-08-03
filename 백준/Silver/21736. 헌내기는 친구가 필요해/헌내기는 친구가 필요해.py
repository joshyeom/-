# 도연이(I)를 matrix에서 찾고 거기서 dfs를 돌려서 P까지 도달하게끔 유도

import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline
h, w = map(int, input().split())




matrix = [list(input().strip()) for _ in range(h)]
dir_ = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(x, y, matrix):
    matrix[y][x] = "."

    count = 0

    for el in dir_:
        new_x = x + el[0]
        new_y = y + el[1]
        
        if 0 <= new_x < w and 0 <= new_y < h:
                value = matrix[new_y][new_x]
                if value == "O":
                    count += dfs(new_x, new_y, matrix)
                elif value == "P":
                    count += 1
                    count += dfs(new_x, new_y, matrix)

    return count



for i in range(len(matrix)):
    if "I" in matrix[i]:
        x = matrix[i].index("I")
        y = i
        total_count = dfs(x, y, matrix)
        
        if total_count > 0:
             print(total_count)
        else:
             print("TT")
        break

