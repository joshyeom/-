from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)  # 최대 힙을 구현하기 위해 음수로 변환하여 추가
        sumEnemy += e  # 총 적의 수를 누적
        if sumEnemy > n:  # 총 적의 수가 n을 초과하면
            if k == 0:  # 사용할 수 있는 기회가 없으면 루프를 종료
                break
            sumEnemy += heappop(heap)  # 최대 힙에서 가장 큰 적의 수를 제거 (실제로는 가장 작은 음수를 제거)
            k -= 1  # 사용할 수 있는 기회 감소
        answer += 1  # 처리한 적의 수 증가
    
    return answer  # 최종 처리한 적의 수 반환