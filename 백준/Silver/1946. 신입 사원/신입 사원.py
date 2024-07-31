# 순위를 비교하고 하나의 종목이라도 낫다면 채용
# 둘다 안되면 불채용
# 시간 복잡도 O(N)

from sys import stdin
input = stdin.readline
N = int(input())

for _ in range(N):
    M = int(input())
    numbers = [list(map(int, input().split())) for _ in range(M)]
    numbers.sort()

    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]

    count = 1
    max_ = numbers[0][1]
    for i in range(1, M):
        if max_ > numbers[i][1]:
            count += 1
            max_ = numbers[i][1]

    print(count)