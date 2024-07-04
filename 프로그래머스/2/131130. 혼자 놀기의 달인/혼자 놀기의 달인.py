from collections import defaultdict


def solution(cards):
  nums = []
  visited = defaultdict(bool)

  answer = 0


  for card in cards:
    if visited[card]:
      continue

    group = []
    next_card = card
    if not visited[next_card]:
      group.append(next_card)
      visited[next_card] = True
      next_card = cards[next_card - 1]

      while not visited[next_card]:
        visited[next_card] = True
        group.append(next_card)
        next_card = cards[next_card - 1]

    nums.append(len(group))

    nums = sorted(nums, reverse=True)


  if len(nums) > 1:
    answer = nums[0] * nums[1]
    return answer
  else:
    return 0
