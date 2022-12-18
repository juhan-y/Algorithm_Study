import heapq
INF = int(1e9)
n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

distance = [INF] * (n+1)

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    
djikstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])