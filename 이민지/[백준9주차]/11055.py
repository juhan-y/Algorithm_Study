import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
d = [0] * n
d[0] = l[0]
for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            d[i] = max(d[i],d[j]+l[i])
        else:
            d[i] = max(d[i],l[i])
print(max(d))

