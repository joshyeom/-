a = map(int, input().split())

# a = [0, 4, 2, 5, 6]

answer = 0

for i in a:
  answer += i * i

answer %= 10

print(answer)