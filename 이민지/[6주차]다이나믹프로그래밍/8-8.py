n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(l[i], m+1):
        if d[j-l[i]] != 10001:
            d[j] = min(d[j], d[j-l[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

