from sys import stdin
input = stdin.readline
N = int(input())

for _ in range(N):
    n = int(input())

    max = 0
    answer = ""
    for _ in range(n):
        univ, num = input().strip().split()
        if max < int(num):
            max = int(num)
            answer = univ
        else:
            pass
    print(answer)