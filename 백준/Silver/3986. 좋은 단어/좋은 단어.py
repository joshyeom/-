import sys
input = sys.stdin.readline
N = int(input())
answer = 0

for _ in range(N):
    stack = []
    words = list(input().strip())

    for word in words:
        if not stack:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    if not stack:
        answer += 1 

print(answer)