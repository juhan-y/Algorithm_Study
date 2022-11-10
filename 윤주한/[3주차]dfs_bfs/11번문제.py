import heapq
INF = int(1e9)
n, m = map(int, input().split())
graph = []
for _ in range(n):
    ls = input()
    temp = []
    for i in ls:
        temp.append(int(i))
    graph.append(temp)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

distance = [[INF] * m for _ in range(n)]

q = []
heapq.heappush(q, (1, 0, 0))
distance[0][0] = 1
while q:
    dist, i, j = heapq.heappop(q)
    if distance[i][j] < dist:
        continue
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            cost = dist + 1
            if cost < distance[ni][nj]:
                distance[ni][nj] = cost
                heapq.heappush(q, (cost, ni, nj))

print(distance[n-1][m-1])