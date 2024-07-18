# 투포인트, 슬라이드 알고리즘으로 불리는 알고리즘
# 배열을 두 포인트로 나누고 하나씩 이동하면서 경우의 수를 찾음

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = list(map(int, input().split()))

# 포인트 초깃값을 할당
left = 0
right = 0
count = 0

# 이동하는 포인트가 수열 범위를 초과할 경우 반복문 탈출
while right < N:
    # 초기 반복문을 위해 right + 1
    num = sum(array[left : right + 1])

    # 값이 같을 경우 정답. 다음 수 탐색을 위해 right + 1
    if num == M:
        count += 1
        right += 1
    
    # num이 작다면 다음 수 탐색을 위해 right + 1
    elif num < M:
        right += 1

    # num이 크다면 비교군 변경을 위해 left += 1
    elif num > M:
        left += 1

print(count)