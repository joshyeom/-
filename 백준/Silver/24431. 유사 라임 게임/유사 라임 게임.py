from sys import stdin
input = stdin.readline
N = int(input())

for _ in range(N):
    n, L, F = map(int, input().strip().split())
    words = list(input().split())
    answer = {}
    count = 0
    for word in words:
        suffix = word[-F:]
        if suffix in answer:
            answer[suffix] += 1
        else:
            answer[suffix] = 1
        
        if answer[suffix] == 2:
            count += 1
            answer[suffix] = 0
    print(count)