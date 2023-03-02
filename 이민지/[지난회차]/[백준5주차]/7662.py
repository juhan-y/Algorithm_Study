import heapq

t = int(input())
min_q = []
max_q = []
visited = [False]*t

for _ in range(t):
    k = int(input())
    for _ in range(k):
        cmd = tuple(input().split())
        n = int(cmd[1])
        if cmd[0] == "I":
            heapq.heappush(min_q, n)
            heapq.heappush(max_q, n)        
        if cmd[0] == "D":
            

