import sys
from collections import deque
input = sys.stdin.readline
letter = input().strip()
N = int(input())


left = deque(list(letter))
right = deque()


for _ in range(N):
    prompt = input().split()
    
    if len(prompt) > 1:
        order, word = prompt
    else:
        order = prompt[0]

    
    if order == "L" and left:
        right.appendleft(left.pop())
    
    elif order == "D" and right:
        left.append(right.popleft())
    
    elif order == "B" and left:
        left.pop()
    
    elif order == "P":
        left.append(word)

print("".join(left + right))
