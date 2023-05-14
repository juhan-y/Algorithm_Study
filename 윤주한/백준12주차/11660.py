n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if i == n-1:
            if j == n-1:
                continue
            graph[i][j] = graph[i][j] + graph[i][j+1]
        elif j == n-1:
            graph[i][j] = graph[i][j] + graph[i+1][j]
        else:
            graph[i][j] = graph[i-1][j] + sum(graph[i][j:])


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(graph[y2-1][x2-1] - graph[y1-1][x1-1])