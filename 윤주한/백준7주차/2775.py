T = int(input())

def calculate(i, j):
    s = 0
    for x in range(1, j+1):
        s += graph[i-1][x]
    return s

graph = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    graph[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        graph[i][j] = calculate(i, j)

for _ in range(T):
    k = int(input())
    n = int(input())

    print(graph[k][n])