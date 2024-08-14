# for문으로 돌면서 했더니 시간초과 발생

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.reverse()

total = 0
count = 0


for coin in coins:
    if K < coin:
        continue

    else:
        count += K // coin
        K %= coin
    
print(count)