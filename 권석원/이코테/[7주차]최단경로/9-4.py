import sys

n,m = map(int,sys.stdin.readline().split())
INF = int(1e9)

graph = [ [] for _ in range(n+1) ]

graph_d = [ INF  ] * (n+1)

for i in range(m):
    st,ed = map(int,sys.stdin.readline().split())
    graph[st].append(ed)
    graph[ed].append(st)
    graph[st].sort()
    graph[ed].sort()
    
x,k = map(int,sys.stdin.readline().split())

visited = [False] * (n+1)

def func(st,cnt):  
    for i in graph[st] :
        if st != i:
            if graph_d[i] > cnt:
                graph_d[i] = cnt               
                func(i,cnt+1)

func(1,1)

k_tmp = graph_d[k]

graph_d = [INF] * (n+1)

func(k,1)

x_tmp = graph_d[x]
ans = k_tmp+x_tmp

if ans < INF:
    print(k_tmp+x_tmp)
else:
    print(-1)
