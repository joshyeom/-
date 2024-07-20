import sys
input = sys.stdin.readline 
n = int(input())


for _ in range(n):
    num, word = input().split()
    num = int(num)
    repeat_word = ""
    for i in range(0, len(word)):
        repeat_word += word[i] * num
    print(repeat_word)