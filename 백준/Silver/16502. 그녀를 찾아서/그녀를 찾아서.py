# 마르코프 체인(Markov chain) 알고리즘
# 마르코프 체인에서는 현재 상태만이 미래 상태에 영향을 미친다는 가정을 합니다. 
# 즉, 과거의 상태는 고려하지 않고 현재 상태에서 다음 상태로의 전이 확률만으로 미래를 예측할 수 있습니다. 
# 이 특성을 무기억성이라고 합니다.

# 가장 간단한 예로, 날씨 예측을 생각해볼 수 있습니다. 
# 오늘의 날씨가 맑을 때 내일의 날씨가 맑을 확률이 0.8이고, 비가 올 확률이 0.2라고 가정합시다.
# 만약 오늘의 날씨가 흐리다면 내일 흐릴 확률이 0.5, 맑을 확률이 0.3, 비가 올 확률이 0.2입니다.
# 이러한 전이 확률을 사용하여 날씨 상태의 변화(전이)를 모델링할 수 있으며, 이를 통해 향후 날씨를 예측할 수 있습니다.

from sys import stdin
input = stdin.readline
T = int(input())
M = int(input())

edges = [tuple(input().strip().split()) for _ in range(M)]

# {'A': {'B': 1.0}, 
# 'B': {'C': 0.3, 'D': 0.7}, 
# 'C': {'A': 0.6, 'D': 0.4}, 
# 'D': {'D': 1.0}}
percentages = {}


# {'A', 'C', 'D', 'B'}
states = set()


for edge in edges:
    start, end, percent = edge
    if start not in percentages:
        percentages[start] = {}
    percentages[start][end] = float(percent)
    states.add(start)
    states.add(end)


answer = [0 for _ in range(len(percentages))]


# ["A", "C", "D", "B"]
states = list(states)
num_states = len(states)


# {'D': 0.25, 'A': 0.25, 'C': 0.25, 'B': 0.25}
initial_prob = {state: 1 / num_states for state in states}

for _ in range(T):

    # {'C': 0, 'A': 0, 'B': 0, 'D': 0}
    new_prob = {state: 0 for state in states}

    for start in percentages:
        for end in percentages[start]:
            new_prob[end] += initial_prob[start] * percentages[start][end]
    initial_prob = new_prob  

for state in sorted(initial_prob):
    
    print(f"{initial_prob[state] * 100:.2f}")