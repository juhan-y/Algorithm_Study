min_ls = []
n, m = map(int, input().split())
graph = []
for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

for i in range(n):
    min_ls.append(min(graph[i]))

print(max(min_ls))