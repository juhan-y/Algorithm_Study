import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)
ans = 0

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):

    if check[i] == 0:
        q = deque()
        q.append(i)
        check[i] = 1

        while q:
            k = q.popleft()

            for v in graph[k]:
                if check[v] == 0:
                    check[v] = 1
                    q.append(v)
        
        ans += 1

print(ans)
        
