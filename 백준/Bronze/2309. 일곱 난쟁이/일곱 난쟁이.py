from sys import stdin
input = stdin.readline

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
total = sum(dwarfs)

for i in range(len(dwarfs)):
    for j in range(i + 1, len(dwarfs)):
        if total - dwarfs[i] - dwarfs[j] == 100:
            for k in range(len(dwarfs)):
                if k == i or k == j:
                    pass
                else:
                    print(dwarfs[k])
            exit()
