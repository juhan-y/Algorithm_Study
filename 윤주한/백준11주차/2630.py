n = int(input())
graph = []
for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

def check_1(x, y, nc):
    for i in range(y, y + nc):
        for j in range(x, x+nc):
            if graph[i][j] == 0:
                return False
    
    return True

def check_0(x, y, nc):
    for i in range(y, y + nc):
        for j in range(x, x+nc):
            if graph[i][j] == 1:
                return False
    
    return True

nc = n
ans_1 = 0
ans_0 = 0
cnt_1 = 0
cnt_0 = 0
while nc >= 1:
    check_ls = []
    for i in range(0, n, nc):
        for j in range(0, n, nc):
            check_ls.append((i, j))
    temp_1 = cnt_1
    temp_0 = cnt_0
    cnt_1 = 0
    cnt_0 = 0

    for y, x in check_ls:
        result_1 = check_1(x, y, nc)
        result_0 = check_0(x, y, nc)
        if result_1:
            cnt_1 += 1
        if result_0:
            cnt_0 += 1
    
    ans_1 += cnt_1 - 4 * temp_1
    ans_0 += cnt_0 - 4 * temp_0

    nc //= 2

print(ans_0)
print(ans_1)