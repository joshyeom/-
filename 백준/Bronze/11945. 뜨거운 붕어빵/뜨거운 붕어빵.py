import sys
input = sys.stdin.readline
N, M = map(int, input().split())


# 출력할 결과물을 저장할 빈 배열 선언
answer = []


for _ in range(0, N):
    # 공백을 지워주는 strip() 함수
    data = input().strip()
    # 공백을 뒤로 바꾸면서 복사해주는 ::-1 기법
    answer.append(data[::-1])
    
    # 각 배열을 문자열로 join 하면서 "\n"줄바꿈 넣기
print("\n".join(answer))