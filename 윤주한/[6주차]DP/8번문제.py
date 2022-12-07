n, m = map(int, input().split())
INF = int(1e9)
d = [INF] * (m+1)
ls = []

for _ in range(n):
    ls.append(int(input()))

for i in ls:
    d[i] = 1

for i in range(1, m+1):
    for j in ls:
        if i >= j:
            d[i] = min(d[i], d[i-j]+1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])