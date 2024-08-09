from sys import stdin
input = stdin.readline

n = int(input())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(n+1): # 상담에 필요한 기간이 퇴사날을 벗어나는 경우 제거
    if i + arr[i][0] > n+1:
        arr[i][1] = 0

for i in range(n): # dp를 이용해 각 날짜의 최댓값을 구하기
    for j in range(i+arr[i][0], n+1):
        if dp[j] < dp[i] + arr[j][1]:
            dp[j] = dp[i] + arr[j][1]

print(max(dp)) # dp의 최댓값 -> 최대비용