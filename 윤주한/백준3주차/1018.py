n, m = map(int, input().split())

graph = []
for _ in range(n):
  a = input()
  temp = []
  for i in a:
    temp.append(i)
  graph.append(temp)

def count_change(i, j):
  cnt = 0
  first = graph[i][j]
  for y in range(i, i+8):
    for x in range(j, j+8):
      if (x + y) % 2 == 0 and graph[y][x] != first:
        cnt += 1
      elif (x + y) % 2 == 1 and graph[y][x] == first:
        cnt += 1
  return min(64-cnt, cnt)

ans = []
for i in range(n-7):
  for j in range(m-7):
    ans.append(count_change(i,j))

print(min(ans))