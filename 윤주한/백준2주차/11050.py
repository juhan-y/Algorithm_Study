n, k = map(int, input().split())

d = [1] * (n+1)

for i in range(1, n+1):
  d[i] = d[i-1] * i

print(int(d[n] / (d[n-k] * d[k])))