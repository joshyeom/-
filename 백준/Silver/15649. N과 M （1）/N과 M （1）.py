# 백 트래킹, 재귀
# 시간복잡도 O(N!)

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# print할 빈 배열
answer = []

def solution():

    # M의 자리 숫자가 되면 print 및 탈출
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return

    # M의 자리 미만이면 요소 추가 및 재귀
    for i in range(1, N + 1):
        if i not in answer:
            answer.append(i)
            solution()
            # 재귀문이 return되면 마지막 요소를 pop
            answer.pop()

solution()