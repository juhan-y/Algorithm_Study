t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for i in range(2):
        graph.append(list(map(int, input().split())))

    d = [[0] * n for _ in range(2)]
    d[0][0] = graph[0][0]
    d[1][0] = graph[1][0]
    for i in range(1, n):
        d[0][i] = max(d[0][i], graph[0][i] + d[1][i-1])
        d[1][i] = max(d[1][i], graph[1][i] + d[0][i-1])
        if i > 1:
            d[0][i] = max(d[0][i], graph[0][i] + d[0][i-2], graph[0][i] + d[1][i-2])
            d[1][i] = max(d[1][i], graph[1][i] + d[0][i-2], graph[1][i] + d[1][i-2])

    print(max(d[0][n-1], d[1][n-1]))