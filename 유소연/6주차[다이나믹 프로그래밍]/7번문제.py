import sys

n = int(sys.stdin.readline())
d = [0]*1001
d[0] = 1
d[1] = 3

for i in range(2,n) :
    d[i] = d[i-1]+d[i-2]+1

print(d[n-1]%796796)