x, y = map(int, input().split())

dates = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

# 7, 8월을 생각못했었음
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = y
for i in range(1, x):
    day += days[i - 1]

print(dates[day % 7])
