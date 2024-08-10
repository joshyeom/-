N, M = map(int, input().split())
friend_map = [[N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    friend_A, friend_B = map(int, input().split())
    friend_map[friend_A-1][friend_B-1] = 1
    friend_map[friend_B-1][friend_A-1] = 1

for k in range(N):  # 경유하는 정점
    for i in range(N):  # 출발 정점
        for j in range(N):  # 도착 정점
            if i == j:
                friend_map[i][j] = 0  # 자기 자신으로 가는 비용은 0
            else:
                friend_map[i][j] = min(friend_map[i][j],
                                       friend_map[i][k] + friend_map[k][j])
                

bacon = []
for row in friend_map:
    bacon.append(sum(row))
print(bacon.index(min(bacon)) + 1)