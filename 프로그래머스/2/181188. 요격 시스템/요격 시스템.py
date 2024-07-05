# 그리디 문제

def solution(targets):
    # 구간을 끝나는 시간 기준으로 정렬
    targets.sort(key=lambda x: x[1])

    cnt, end = 0, 0
    # 
    for s, e in targets:
      if s >= end:
          cnt += 1
          end = e
    return cnt