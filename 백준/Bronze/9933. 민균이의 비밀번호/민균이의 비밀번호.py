from sys import stdin
input = stdin.readline
N = int(input().strip())


arr = [input().strip() for _ in range(N)]

for el in arr:
    try:
        reversed_el = el[::-1]
        answer_index = arr.index(reversed_el)
        answer = arr[answer_index]
        print(len(answer), el[len(el) // 2])
        break
    except ValueError:
        continue