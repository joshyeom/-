from sys import stdin
input = stdin.readline
N = int(input())

gift = []

for _ in range(N):
    new_input = list(map(int, input().split()))


    if new_input[0] == 0 and not gift:
        print(-1)
    
    elif new_input[0] == 0:
        print(gift.pop())

    else:
        for _ in range(new_input[0]):
            gift.append(new_input.pop())
        gift.sort()