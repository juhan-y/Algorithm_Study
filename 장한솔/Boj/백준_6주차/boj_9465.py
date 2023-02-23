import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    num = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    graph = [[0] * N for _ in range(2)]

    graph[0][0], graph[1][0] = num[0][0], num[1][0]
    if N >= 2 :
        graph[0][1] = graph[1][0] + num[0][1]
        graph[1][1] = graph[0][0] + num[1][1]

    if N >= 3 :
        for i in range(2, N) :
            graph[0][i] = max(graph[1][i-2], graph[1][i-1]) + num[0][i]
            graph[1][i] = max(graph[0][i-2], graph[0][i-1]) + num[1][i]

    print(max(graph[0][-1], graph[1][-1]))