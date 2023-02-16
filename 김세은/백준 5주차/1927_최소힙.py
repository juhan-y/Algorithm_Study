# 1927 최소 힙
import sys
import heapq

N = int(input())

heap = []
for i in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(heap, x)
 
    elif x == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
