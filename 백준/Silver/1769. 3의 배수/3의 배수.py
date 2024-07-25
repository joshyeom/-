import sys
input = sys.stdin.readline
N = input().strip()


def solution(num, count):
    
    if len(num) == 1:
        return [str(count), "YES" if int(num) % 3 == 0 else "NO"]

    new_num = list(map(int, num))
    new_num = sum(new_num)
    new_num = str(new_num)


    return solution(new_num, count + 1)

answer = solution(N, 0)

print("\n".join(answer))