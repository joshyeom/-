import sys
input = sys.stdin.readline
N = int(input())

array = [input().split() for _ in range(N)]


for i, el in enumerate(array, 1):
    answer = el[::-1]
    print(f'Case #{i}: {" ".join(answer)}')