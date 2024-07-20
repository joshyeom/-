import sys
input = sys.stdin.readline 
n = int(input())

dict = {}

for _ in range(n):
    fruit, num = input().split()
    num = int(num)
    
    dict[fruit] = dict.get(fruit, 0) + num


for i, (fruit, num) in enumerate(dict.items()):
    if num == 5:
        print("YES")
        break
    # 마지막 항목인지 확인
    if i == len(dict) - 1:
        print("NO")