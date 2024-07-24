import sys
input = sys.stdin.readline
N = int(input())
enter = input()

sets = []
count = set([])

for i in range(N - 1):
    str = input().strip()

    if str == "ENTER":
        sets.append(count)
        count = set([])
    else:
        count.add(str)


if count:
    sets.append(count)


print(sum(len(s) for s in sets))