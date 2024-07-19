import sys
input = sys.stdin.readline
n = int(input())

place = (n - 1) * 4 + 1
mid = n * 2 - 1

star = "*"
space = " "

left = []
right = []

for i in range(1, mid + 1):
    if i % 2 == 1:
        print("".join(left) + star * place + "".join(right))
        left.append(star)
        right.insert(0, star)
    
    else:
        print("".join(left) + space * place + "".join(right))
        left.append(space)
        right.insert(0, space)
    
    place -= 2


for i in range(mid + 1, (n - 1) * 4 + 2):
    if i % 2 == 1:
        place += 2
        left.pop()
        right.pop(0)
        print("".join(left) + star * place + "".join(right))
    
    else:
        place += 2
        left.pop()
        right.pop(0)
        print("".join(left) + space * place + "".join(right))