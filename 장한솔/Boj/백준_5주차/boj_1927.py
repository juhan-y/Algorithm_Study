import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N) :
    i = int(sys.stdin.readline())
    if i == 0 :
        if heap :
            print(heapq.heappop(heap))
        else :
            print(0)
    else :
        heapq.heappush(heap, i)