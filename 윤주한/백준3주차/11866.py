n, k = map(int, input().split())

ls = [i for i in range(1, n+1)]

ans = []
while len(ans) != n:
  ans.append(ls[k-1])
  ls = ls[k:] + ls[:k-1]
  for i in ls:
    if i in ans:
      ls.remove(i)
  if len(ls) == 0:
    break
  while len(ls) < k:
    ls += ls
print('<', end='')
for i in range(n):
  if i != n-1:
    print(ans[i], end=', ')
  else:
    print(f'{ans[i]}>')