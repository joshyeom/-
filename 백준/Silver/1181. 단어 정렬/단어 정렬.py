from sys import stdin
input = stdin.readline
N = int(input())

words = set([input().strip() for _ in range(N)])
words = list(words)
words.sort(key=lambda x: (len(x), x))

print("\n".join(words))