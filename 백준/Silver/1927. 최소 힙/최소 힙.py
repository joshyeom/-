from sys import stdin
input = stdin.readline
N = int(input())
import heapq

heap = []
heapq.heapify(heap)

for _ in range(N):
    num = int(input())
    if num == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, num)
