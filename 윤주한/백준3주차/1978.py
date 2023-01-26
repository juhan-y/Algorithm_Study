n = int(input())

ls = list(map(int, input().split()))

maxi = max(ls)
d = [1] * (maxi + 1)
d[1] = 0
for i in range(2, int(maxi ** 0.5) + 1):
  if d[i] == 1:
    for j in range(i+i, maxi+1, i):
      d[j] = 0

cnt = 0
for i in ls:
  if d[i] == 1:
    cnt += 1

print(cnt)