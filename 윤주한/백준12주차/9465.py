t = int(input())

for _ in range(t):
    graph = []
    n = int(input())
    for _ in range(2):
        graph.append(list(map(int, input().split())))

    
    if n != 1:
        graph[0][1] += graph[1][0]
        graph[1][1] += graph[0][0]
        for j in range(2, n):
            graph[0][j] = graph[0][j] + max(graph[1][j-1], graph[1][j-2])
            graph[1][j] = graph[1][j] + max(graph[0][j-1], graph[0][j-2])
        
    print(max(max(graph[0]), max(graph[1])))
