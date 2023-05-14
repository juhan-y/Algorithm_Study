n, m = map(int, input().split())

graph = []
for _ in range(n):
  ls = input()
  temp = []
  for j in ls:
    temp.append(int(j))
  graph.append(temp)

for i in range(1, n):
  for j in range(1, m):
    if graph[i][j] == 1:
      graph[i][j] = min(graph[i-1][j-1], graph[i-1][j], graph[i][j-1]) + 1
      


maxi = 0
for i in range(n):
  maxi = max(maxi, max(graph[i]))
print(maxi ** 2)