from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

reverse_A = list(reversed(sorted(A)))
sort_B = sorted(B)

answer = 0

for i in range(N):
    answer += reverse_A[i] * sort_B[i]

print(answer)