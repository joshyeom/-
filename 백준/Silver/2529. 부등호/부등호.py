import sys

# 표준 입력으로부터 데이터를 읽어오기 위해 설정
input = sys.stdin.readline

# 부등호 개수 입력 받기
k = int(input())

# 부등호 리스트 입력 받기
signs = list(input().split())

# 두 숫자와 부등호 연산자를 받아 조건을 체크하는 함수
def check(a, b, op):
    if op == '<':
        if a > b: 
            return False
    if op == '>':
        if a < b: 
            return False
    return True

def dfs(cnt, num):
    # 모든 자리수를 다 채웠다면 결과 리스트에 추가
    if cnt == k + 1:
        answer.append(num)
        return
    
    # 0부터 9까지 숫자를 순회
    for i in range(10):
        # 이미 사용한 숫자라면 패스
        if visited[i]: 
            continue
        
        # 첫 자리이거나 현재 자리의 부등호 조건을 만족한다면
        if cnt == 0 or check(num[cnt-1], str(i), signs[cnt-1]):
            # 숫자 사용 표시
            visited[i] = 1
            # 다음 자리로 이동하며 재귀 호출
            dfs(cnt+1, num+str(i))
            # 숫자 사용 표시 해제 (백트래킹)
            visited[i] = 0

# 숫자 사용 여부를 기록하는 리스트 초기화
visited = [0] * 10

# 결과를 저장할 리스트 초기화
answer = []

# DFS 탐색 시작 (자리수 0, 빈 문자열부터 시작)
dfs(0, '')

# 결과 리스트를 정렬하여 최대값과 최소값을 구하기
answer.sort()

# 최대값 출력
print(answer[-1])

# 최소값 출력
print(answer[0])
