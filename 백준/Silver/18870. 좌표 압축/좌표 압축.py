# set을 사용 안하니 인덱싱 문제 발생해서 set으로 다시 품
# 시간복잡도 O(N)

from sys import stdin
input = stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(set(numbers))

dict_ = {}
idx = 0

for value in sorted_numbers:
    if value not in dict_:
        dict_[value] = idx
    idx += 1


answer = []

for num in numbers:
    answer.append(dict_[num])

print(" ".join(map(str, answer)))