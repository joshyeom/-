a = list(map(int, input().split()))
b = int(input())

total = (a[0] * 60 * 60) + (a[1] * 60) + a[2] + b

hour = total // (60 * 60)
minute = (total % (60 * 60)) // 60
second = total % 60

if hour >= 24:
  hour %= 24

print(hour, minute, second)