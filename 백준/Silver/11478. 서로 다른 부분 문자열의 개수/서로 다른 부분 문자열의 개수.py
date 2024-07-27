from sys import stdin
input = stdin.readline

str = input().strip()

arr = set()

count = 0

while True:
    count += 1
    for i in range(len(str)):
        if count + i < len(str) + 1:
            arr.add(str[i:i + count])

    if count > len(str) + 1:
        break

print(len(arr))
