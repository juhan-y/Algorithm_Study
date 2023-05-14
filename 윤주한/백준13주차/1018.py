n, m = map(int, input().split())

graph = []
for _ in range(n):
    temp = input()
    temp_ls = []
    for i in temp:
        temp_ls.append(i)
    graph.append(temp_ls)

def check(y, x):
    cnt = 0
    ans = [graph[y][x], 'W' if graph[y][x] == 'B' else 'B']
    idx = 0
    for i in range(y,8+y):
        if i % 2 == 1:
            idx = 1
        else:
            idx = 0
        for j in range(x,8+x):
            if graph[i][j] != ans[idx]:
                cnt += 1
            idx += 1
            if idx == 2:
                idx = 0
        
    return min(cnt, 64-cnt)
    
ans = 1e9
for i in range(n-7):
    for j in range(m-7):
        ans = min(ans, check(i,j))

print(ans)