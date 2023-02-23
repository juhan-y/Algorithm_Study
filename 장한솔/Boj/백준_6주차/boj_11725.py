import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
root = [0] * (N+1)

for _ in range(N-1) :
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(a) : # a의 자식 다 돌면서 내가 부모다 입력해주기
    for i in graph[a] :
        if root[i] == 0:
            root[i] = a
            dfs(i)

dfs(1)

print(*root[2:], sep = "\n")