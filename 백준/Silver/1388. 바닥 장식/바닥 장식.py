from sys import stdin
input = stdin.readline

col, row = map(int, input().split())

map = [input().strip() for _ in range(col)]
count = 0
visited = []  # visited를 리스트로 유지


def solution(dir, x, y):

    new_x = x
    new_y = y

    if dir == "-":
        new_x += 1
    elif dir == "|":
        new_y += 1 

    if new_x >= row or new_y >= col:
        return


    if dir == "-" and map[y][new_x] == "-":
        if [y, new_x] not in visited:  
            visited.append([y, new_x]) 
            solution("-", new_x, y)
    elif dir == "|" and map[new_y][x] == "|":
        if [new_y, x] not in visited:  
            visited.append([new_y, x]) 
            solution("|", x, new_y)


for i in range(col):
    for j in range(row):
        if [i, j] not in visited:  
            if map[i][j] == "-":
                visited.append([i, j])  
                solution("-", j, i) 
                count += 1
            elif map[i][j] == "|":
                visited.append([i, j])  
                solution("|", j, i)
                count += 1

print(count)
