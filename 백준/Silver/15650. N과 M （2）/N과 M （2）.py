# 재귀 안에 2개의 반복문 O(N! + 2N)


import sys
input = sys.stdin.readline
N, M = map(int, input().split())

answer = []

def solution():

    if len(answer) == M:
        # answer = list(map(str, answer))
        
        for i in range(0, len(answer) - 1):
            if answer[i] > answer[i + 1]:
                return
        
        print(" ".join(map(str, answer)))



    for i in range(1, N + 1):
        if i not in answer:
            answer.append(i)
            solution()
            answer.pop()

solution()