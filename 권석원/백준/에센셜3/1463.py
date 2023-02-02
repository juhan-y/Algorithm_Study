import sys
    
N = int(sys.stdin.readline())

d = [N for _ in range(N+1)]

d[N] = 0

for i in range(N,0,-1):
    if i % 3 == 0 :
        d[i//3] = min(d[i] + 1,d[i//3])
    if i % 2 == 0 : 
        d[i//2] = min(d[i] + 1,d[i//2])
    
    d[i-1] = min(d[i] + 1,d[i-1])

print(d[1])

