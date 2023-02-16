import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())

graph = [[] for _ in range(200001)]

for i in range(100001):
    if i > 0:
        graph[i].append(i-1)
        graph[i].append(i*2)
    graph[i].append(i+1)
INF = int(1e9)
d = [INF] * 200001

q = []
heapq.heappush(q, (0, n))
d[n] = 0
while q:
    cnt, now = heapq.heappop(q)
    if d[now] < cnt:
        continue
    for i in graph[now]:
        cost = cnt + 1
        if d[i] > cost:
            d[i] = cost
            heapq.heappush(q, (cost, i))

print(d[k])