import math

# [x, y]형태로 모두 만들어서 len을 구하려고 했지만 시간초과로 fail
# 만들지 않고 x형태에서 y를 비교 후 count하는 식으로 변경

def solution(k, d):
    answer = 0
    
    # 0부터 d + 1까지 range를 k배수로
    for x in range(0, d + 1, k):
      #현재 x에서 최대 y값을 구함
        max_y = math.sqrt(d**2 - x**2)
        # y값은 '0'도 포함이라 '+1'로 추가
        count_y = int(max_y // k) + 1
        answer += count_y
    
    return answer