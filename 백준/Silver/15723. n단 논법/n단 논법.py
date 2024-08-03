from sys import stdin
input = stdin.readline

N = int(input())
dict_ = {}

for _ in range(N):
    str_ = list(input().strip().split())
    key = str_[0] 
    value = str_[2] 

   
    dict_[key] = value

M = int(input())

for _ in range(M):
    str_ = list(input().strip().split())
    key = str_[0] 
    value = str_[2] 

    count = 0
    while count < len(dict_):
        if key not in dict_:
            print("F")
            break

        new_value = dict_[key]

        if new_value == value:
            print("T")
            break

        else:
            key = new_value
            count += 1