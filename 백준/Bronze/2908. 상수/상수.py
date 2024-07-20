import sys
input = sys.stdin.readline 
first, second = input().split()

first = list(reversed(first))
second = list(reversed(second))

first = int("".join(first))
second = int("".join(second))

print(max(first,second))