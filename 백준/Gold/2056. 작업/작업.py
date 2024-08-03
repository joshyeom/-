import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * (N + 1)
for i in range(1, N + 1):

    # 언패킹(unpacking) 연산자 나머지 모든 값을 pre라는 리스트에 할당하는 것을 의미
    work, count, *pre = map(int, input().split())

    dp[i] = work
    for j in pre:
        dp[i] = max(dp[i], dp[j] + work)

#dp =  [0, 5, 6, 9, 11, 12, 19, 23]

print(max(dp))