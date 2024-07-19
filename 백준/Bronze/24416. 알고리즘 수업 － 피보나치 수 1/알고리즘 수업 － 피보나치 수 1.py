# 각 함수를 돌면서 count를 +1 했지만 시간 초과
# 반복문을 돌지 않고 반복문의 값을 유추해야 함

import sys
input = sys.stdin.readline
n = int(input())

f = [0] * (n + 1)


# DP를 이용한 풀이
def fib(n):
    f[1] = 1
    f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


# 동적 프로그래밍의 단순히 반복 횟수만 구하면 되기 때문에 n -2
# 1, 2를 제외한 나머지 반복횟수
def fibonacci(n):
    return n - 2


print(fib(n), fibonacci(n))