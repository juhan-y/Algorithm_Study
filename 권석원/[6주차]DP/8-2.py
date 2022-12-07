import sys

n = int(sys.stdin.readline())

d = []
d.append(0)
d.append(1)
d.append(1)

for i in range(2,n+1):
    d.append(d[i] + d[i-1])
    
print(d[n])
