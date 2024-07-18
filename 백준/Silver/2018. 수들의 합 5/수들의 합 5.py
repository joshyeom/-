# 전 수열과 마찬가지로 투 포인트로 하나씩 모은다음에 값이 같으면 카운트하고 넘거나 아니라면 포인터를 움직이는 형식

## fail 1
## 리스트를 생성해서 풀었더니 메모리 초과 발생, 배열없이 반복문을 돌아야 함

import sys
input = sys.stdin.readline
N = int(input())

# 마지막은 항상 정답이기에 1
answer = 1

# 초기값 지정
left = 1
right = 2 
total = 3


while left < N - 1 and right < N:

    # 값이 작다면 right를 옮김
    # total += right
    if total < N:
        right += 1
        total += right

    else:
        # 값이 같다면 answer += 1
        if total == N:
            answer += 1

        # total이 크다면 left를 키워주고 total에서는 전에 left를 빼줌
        total -= left
        left += 1
    

print(answer)