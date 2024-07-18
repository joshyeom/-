import sys
input = sys.stdin.readline 
num = int(input())

## 별과 공백을 상수로 선언
STAR = "*"
SPACE = " "

## 0으로 시작하면 빈 줄을 찍음
for i in range(1, num + 1):
    ## print할 answer 선언
    left = []
    right = []

    # i만큼 반복
    for _ in range(0, i):
        left.append(STAR)
        right.append(STAR)
    
    for _ in range(num - i):
        left.append(SPACE)
        right.insert(0, SPACE)

    answer = "".join(left) + "".join(right)

    # 만들어진 별만큼 출력
    print(answer)

for i in range(1, num):
    ## print할 answer 선언
    left = []
    right = []

    # i만큼 반복
    for _ in range(num - i):
        left.append(STAR)
        right.append(STAR)
    
    for _ in range(0, i):
        left.append(SPACE)
        right.insert(0, SPACE)

    answer = "".join(left) + "".join(right)

    # 만들어진 별만큼 출력
    print(answer)
