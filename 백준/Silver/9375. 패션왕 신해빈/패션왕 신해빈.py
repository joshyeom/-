from sys import stdin
input = stdin.readline
from collections import defaultdict
N = int(input())

for _ in range(N):
    num_clothes = int(input())
    dict = defaultdict(list)
    for _ in range(num_clothes):
        name, part = input().strip().split()
        dict[part].append(name)
    
    count = 1

    for part, names in dict.items():
        count *= (len(names) + 1)
    print(count - 1)