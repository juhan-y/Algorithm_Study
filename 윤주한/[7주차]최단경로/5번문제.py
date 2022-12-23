import heapq
n, m, c = map(int, input().split())

INF = int(1e9)

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

def djikstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[start]:
            continue
        for i in graph[node]:
            cost = i[0] + dist
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
djikstra(c)

ans = [i for i in distance if i < INF]
print(len(ans) - 1, max(ans))