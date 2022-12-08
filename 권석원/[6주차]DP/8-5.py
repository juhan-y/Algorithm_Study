import sys

n = int(sys.stdin.readline())

def func(k,cnt,ans = []):
    
    a,b,c,d = 9999999,9999999,9999999,9999999
    
    if k == 1:
        return cnt
    
    if k % 5 == 0:
        a = func(k//5,cnt+1)
    if k % 3 == 0:
        b = func(k//3,cnt+1)
    if k % 2 == 0:
        c = func(k//2,cnt+1)
    if k - 1 >= 1:
        d = func(k-1,cnt+1)

    return min(a,b,c,d)

print(func(n,0))