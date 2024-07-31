import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    L = [0 for __ in range(n+1)]
    for i in range(n):
        a, b = map(int, input().split())
        L[a]=b
    min_rank = L[1]
    cnt = 1
    for j in range(2, n+1):
        if min_rank>L[j]:
            cnt+=1
            min_rank=L[j]
    print(cnt)