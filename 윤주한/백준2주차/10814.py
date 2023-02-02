n = int(input())
cnt = 0
ls = []
for _ in range(n):
  a, b = input().split()
  temp = [int(a), b]
  temp.append(cnt)
  cnt += 1
  ls.append(temp)

ls.sort(key = lambda x: (x[0], x[2]))

for i in ls:
  print(i[0], i[1])