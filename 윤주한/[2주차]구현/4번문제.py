import copy
n, m = map(int, input().split())
i, j, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

visited = copy.deepcopy(graph)

ans = 1
cnt = 0
while True:
    k -= 1
    if k < 0:
        k = 3
    if cnt < 4:
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            if visited[ni][nj] == 0:
                i, j = ni, nj
                visited[ni][nj] = 1
                ans += 1
                cnt = 0
            else:
                cnt += 1
        else:
            cnt += 1
    else:
        ni = i - di[k]
        nj = j - dj[k]
        if graph[ni][nj] == 1:
            break
        cnt = 0
        
print(ans)