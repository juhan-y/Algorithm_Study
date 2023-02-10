# 방법 1 : dfs
import sys
sys.setrecursionlimit(5000) # dfs, 재귀 사용시 필수
input = sys.stdin.readline # readline 사용 권장

def dfs(v, d):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i, d+1)

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
            cnt += 1
        else:
            dfs(i,0)
            cnt += 1
print(cnt)