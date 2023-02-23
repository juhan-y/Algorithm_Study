import sys
from collections import deque

N = int(sys.stdin.readline())

tree_list = [ [] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    tree_list[a].append(b)
    tree_list[b].append(a)


ans = [0] * (N+1)

q = deque([1])
visited = [False] * (N+1)
while q:
    k = q.pop()

    for node in tree_list[k]:
        if not visited[node]:
            ans[node] = k
            visited[node] = True
            q.append(node)

for i in range(2,N+1):
    print(ans[i])

