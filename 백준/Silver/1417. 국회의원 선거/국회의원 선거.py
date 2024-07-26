from sys import stdin
input = stdin.readline
N = int(input())

arr = [int(input()) for _ in range(N)]

count = 0

while True:
    maximum_index = arr.index(max(arr))

    if maximum_index != 0:
        arr[0] += 1
        arr[maximum_index] -= 1
        count += 1
    else:
        for i in range(1, len(arr)):
            if arr[i] == arr[maximum_index]:
                arr[i] -= 1
                arr[0] += 1
                count += 1
                break
        print(count)
        break