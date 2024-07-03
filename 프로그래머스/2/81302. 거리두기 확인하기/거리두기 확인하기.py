from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j]) # P좌표들을 start에 저장


    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1  # 방문 처리
        
        while queue:
          # queue에서 첫 번째 리스트를 꺼내서 y와 x로 할당
            y, x = queue.popleft()
        
            
            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4): # [0,1,2,3,4]

                nx = x + dx[i] # x좌표 변경
                ny = y + dy[i] # y좌표 변경

                # 각 좌표가 0 ~ 4까지에 숫자이고 방문하지 않았다면
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:

                    #방문한 좌표가 "O"일 경우 
                    if p[ny][nx] == 'O':

                        # 큐에 추가
                        queue.append([ny, nx])

                        # 방문에 추가
                        visited[ny][nx] = 1
                        
                        #거리 +1
                        distance[ny][nx] = distance[y][x] + 1
                    

                    #방문한 좌표가 P인데, 거리가 0 또는 1일 경우
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    
    #모든 P의 거리가 2 이상일 경우
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer
