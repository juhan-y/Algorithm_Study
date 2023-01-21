n = int(input())
ls = []
for _ in range(n):
  x, y = map(int, input().split())
  ls.append([x,y])

ls.sort(key = lambda k: (k[0], k[1]))

for i in ls:
  a, b = i
  print(a, b)