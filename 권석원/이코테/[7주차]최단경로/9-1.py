import sys

num_node,cnt = map(int,sys.stdin.readline().split())

start = int(sys.stdin.readline())
INF = int(1e9)

graph = [ [] for _ in range(num_node+1)]
graph_w = [ [0]*(num_node+1) for _ in range(num_node+1)]

w_lst = [INF] * (num_node+1)
visited = [False] * (num_node+1)

for i in range(cnt):
    st,ed,w = map(int,sys.stdin.readline().split())
    graph[st].append(ed)
    graph[st].sort()
    graph_w[st][ed] = w
 
w_lst[start] = 0

def func(st): 
    visited[st] = True
    changed = [False] * (num_node+1)
    tmp_list = []
    
    for ed in graph[st]:        
        if visited[ed] == False:
            tmp = w_lst[st] + graph_w[st][ed]
            if w_lst[ed] >= tmp:
                w_lst[ed] = tmp
                changed[ed] = True
    
    min_val = INF
    
    for i in range(1,num_node):
        if visited[i] == False and changed[i]:
            if min_val != min(w_lst[i],min_val):  
                tmp_list.clear() 
                tmp_list.append(i)
                min_val = w_lst[i]
            elif min_val == w_lst[i]:
                tmp_list.append(i)

    
    tmp_list.sort()
    
    for idx in tmp_list:
        func(idx)

func(start)

    
for i in range(1,num_node+1):
    print(w_lst[i])
        
    
    

    
    


