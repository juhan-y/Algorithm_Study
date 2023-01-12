from queue import PriorityQueue
import sys

n,m,c = map(int,sys.stdin.readline().split())

INF = int(1e9)

graph = [ [] for _ in range(n+1) ]
graph_w = [ [0]*(n+1) for _ in range(n+1) ]
w_lst = [INF] * (n+1)
visited = [False] * (n+1)

for i in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[x].sort()
    graph_w[x][y] = z
    

que = PriorityQueue()
que.put((0,c))
w_lst[c] = 0

cnt = -1

while que.empty() == False:
    
    st = que.get()[1]
    
    if visited[st] == True:
        continue
    
    cnt += 1
    
    visited[st] = True
    
    for ed in graph[st]:        
        if visited[ed] == False:
            tmp = w_lst[st] + graph_w[st][ed]
            if w_lst[ed] >= tmp:
                w_lst[ed] = tmp
                que.put((tmp,ed))
    
if INF in w_lst:
    w_lst.remove(INF)

print(cnt,max(w_lst))