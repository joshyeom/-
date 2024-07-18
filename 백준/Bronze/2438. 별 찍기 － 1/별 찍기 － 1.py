import sys
input = sys.stdin.readline 
num = int(input())

## 별을 상수로 선언
STAR = "*"

## 0으로 시작하면 빈 줄을 찍음
for i in range(1, num + 1):
    ## print할 answer 선언
    answer = ""

    # i만큼 반복
    for _ in range(0, i):
        answer += STAR
    
    # 만들어진 별만큼 출력
    print(answer)
