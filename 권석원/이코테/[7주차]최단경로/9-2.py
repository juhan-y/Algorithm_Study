from queue import PriorityQueue
import sys

num_node,cnt = map(int,sys.stdin.readline().split())

start = int(sys.stdin.readline())
INF = int(1e9)

graph = [ [] for _ in range(num_node+1) ]
graph_w = [ [0]*(num_node+1) for _ in range(num_node+1) ]

w_lst = [INF] * (num_node+1)
visited = [False] * (num_node+1)

for i in range(cnt):
    st,ed,w = map(int,sys.stdin.readline().split())
    graph[st].append(ed)
    graph[st].sort()
    graph_w[st][ed] = w

que = PriorityQueue()
w_lst[start] = 0

que.put((0,start))

while que.empty() == False:
    
    st = que.get()[1]
    
    if visited[st] == True:
        continue
    
    visited[st] = True
    
    for ed in graph[st]:        
        if visited[ed] == False:
            tmp = w_lst[st] + graph_w[st][ed]
            if w_lst[ed] >= tmp:
                w_lst[ed] = tmp
                que.put((tmp,ed))



for i in range(1,num_node+1):
    print(w_lst[i])



