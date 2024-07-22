import sys
input = sys.stdin.readline

cards = int(input())
deck = list(map(int, input().split()))

list_dict = {}

for i in range(0, cards):
    list_dict[deck[i]] = list_dict.get(deck[i], 0) + 1


must_cards = int(input())
must_deck = list(map(int, input().split()))

answer = []

for card in must_deck:
    if list_dict.get(card, 0) > 0:
        answer.append(f"{list_dict.get(card, 0)}")
    else:
        answer.append("0")

print(" ".join(answer))