# 배열을 만든 뒤 순회하며 높은 값들을 카운트
# O(2N)

import sys
input = sys.stdin.readline
N = int(input())

# 배열을 만들고 역순 정렬
bars = [int(input()) for _ in range(N)]
bars = bars[::-1]

# 맨 처음 보이는 막대부터 카운트
# 6, 9, 8, 7 반례를 찾아 current_max 추가
count = 0
current_max = 0

# 맨 앞 요소보다 클 경우 count += 1
for bar in bars:
    if current_max < bar:
        current_max = bar
        count += 1

print(count)