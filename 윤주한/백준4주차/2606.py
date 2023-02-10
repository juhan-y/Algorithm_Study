n = int(input())

comps = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    comps[a].append(b)
    comps[b].append(a)

visited = [False] * (n+1)

def dfs(n):
    for i in comps[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

visited[1] = True
dfs(1)
print(visited.count(True)-1)
