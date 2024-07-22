import sys
input = sys.stdin.readline

cards = int(input())
deck = list(map(int, input().split()))

list_dict = {}

for i in range(0, cards):
    list_dict[deck[i]] = list_dict.get(deck[i], True)


must_cards = int(input())
must_deck = list(map(int, input().split()))

answer = []

for i in range(0,must_cards):
    if list_dict.get(must_deck[i]):
        answer.append("1")
    else:
        answer.append("0")

print(" ".join(answer))