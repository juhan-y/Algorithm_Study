import sys

N = int(sys.stdin.readline())
p_num = int(sys.stdin.readline())

com = [[] for i in range(N+1)]
visited = [False] * (N+1)

for _ in range(p_num) :
    i, j = map(int, sys.stdin.readline().split())
    com[i].append(j)
    com[j].append(i)

def virus(v) :
    visited[v] = True
    for i in com[v] :
        if visited[i] == False :
            virus(i)

virus(1)
print(sum(visited) - 1)