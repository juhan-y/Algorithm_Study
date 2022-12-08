n = int(input())
ls = list(map(int, input().split()))

d = ls.copy()
d[2] = d[0] + ls[2]
for i in range(3, n):
    d[i] = max(d[i-1], d[i-2] + ls[i])
    
print(max(d))