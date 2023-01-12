import sys

t = int(sys.stdin.readline())

for i in range(t):
    h,w,n = map(int,sys.stdin.readline().split())
    
    if n > h:
        Y = n%h
        if Y == 0:
            Y = h
            X = n//h
        else:
            X = n//h + 1
    else:
        Y = n
        X = 1
    
    ans = (Y*100)+X
    
    print(ans)