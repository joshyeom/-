def solution(sequence, k):
    start = 0
    current_sum = 0
    answer = [0, len(sequence) - 1]  # 최소 길이로 초기화
    
    for end in range(len(sequence)):
        current_sum += sequence[end]
        
        while current_sum > k:
            current_sum -= sequence[start]
            start += 1
        
        if current_sum == k:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
    
    return [answer[0], answer[1]]
        