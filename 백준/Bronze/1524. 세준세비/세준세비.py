# reverse=True를 사용해 pop(-1)의 시간초과를 피함
# 시간 복잡도 O(N)

from sys import stdin
input = stdin.readline
N = int(input())

for _ in range(N):
    space = input()
    sejun_num, sebi_num = map(int, input().split())
    
    sj = sorted(list(map(int, input().split())), reverse=True)
    sb = sorted(list(map(int, input().split())), reverse=True)

    while sj and sb:
        if sj[-1] >= sb[-1]:	
            sb.pop()
        else :
            sj.pop()
    
    if sj :
        print('S')
    elif sb :
        print('B')
    else :
        print('C')
       