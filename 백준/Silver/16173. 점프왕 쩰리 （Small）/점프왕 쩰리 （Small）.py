from sys import stdin
input = stdin.readline
N = int(input())

map = [list(map(int,input().split())) for _ in range(N)]


def solution(x, y):

    if map[y][x] == 0:
        print("Hing")
        exit()

    if map[y][x] == -1:
        print("HaruHaru")
        exit()

    jump = map[y][x]
    new_x = x + jump
    new_y = y + jump

    if new_x < N:
        solution(new_x, y)

    if new_y < N:
        solution(x, new_y)


solution(0, 0)

print("Hing")

# [1, 1, 10]
# [1, 5,  1]
# [2, 2, -1]