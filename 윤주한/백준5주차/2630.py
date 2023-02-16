import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def check(k, i, j):
    first = graph[i][j]
    for y in range(i, i+k):
        for x in range(j, j+k):
            if first != graph[y][x]:
                return False
    return True

k = 1
cnt_1 = 0
cnt_0 = 0

while k <= n:
    temp_1 = 0
    temp_0 = 0
    for i in range(0, n, k):
        for j in range(0, n, k):
            if k != 1:
                result = check(k, i, j)
                if result:
                    if graph[i][j] == 1:
                        temp_1 += 1
                    else:
                        temp_0 += 1
            else:
                if graph[i][j] == 1:
                    cnt_1 += 1
                else:
                    cnt_0 += 1
    if k != 1:
        cnt_1 = cnt_1 - temp_1 * 4 + temp_1
        cnt_0 = cnt_0 - temp_0 * 4 + temp_0
    k *= 2

print(cnt_0)
print(cnt_1)
