def solution(picks, minerals):
    # 피로도 표
    fatigue = {
        'diamond': {'diamond': 1, 'iron': 1, 'stone': 1},
        'iron': {'diamond': 5, 'iron': 1, 'stone': 1},
        'stone': {'diamond': 25, 'iron': 5, 'stone': 1}
    }

    def dfs(index, fatigue_sum, picks_left):
        # 더 이상 캘 광물이 없거나 곡괭이가 없을 때
        if index >= len(minerals) or all(p == 0 for p in picks_left):
            return fatigue_sum

        min_fatigue = float('inf')
        for i in range(3):
            if picks_left[i] > 0:
                # 곡괭이를 사용
                picks_left[i] -= 1
                current_fatigue = 0
                next_index = index

                # 현재 곡괭이로 5개의 광물을 캡니다.
                for _ in range(5):
                    if next_index >= len(minerals):
                        break
                    current_fatigue += fatigue[['diamond', 'iron', 'stone'][i]][minerals[next_index]]
                    next_index += 1

                # 다음 단계로 넘어갑니다.
                min_fatigue = min(min_fatigue, dfs(next_index, fatigue_sum + current_fatigue, picks_left))

                # 곡괭이를 원상태로 되돌립니다.
                picks_left[i] += 1

        return min_fatigue

    return dfs(0, 0, picks)