# 11279 최대 힙
import sys
import heapq

N = int(input())

heap = []
for i in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        # 튜플을 원소로 추가하거나 삭제하면 튜플 내에서 맨 앞에 있는 값을
        # 기준으로 최소 힙이 구성됨
        heapq.heappush(heap, (-x, x))   # (우선순위, 값)
 
    elif x == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
