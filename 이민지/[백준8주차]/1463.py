# 방법 1
import sys
n = int(sys.stdin.readline())
d = [0] * (n+1)
for i in range(2, n+1):
    d[i] = d[i-1] +1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[n])


# 방법 2
n = int(input())
d = {1:0}
def ans(n):
    if n in d:
        return d[n]
    if n%2==0 and n%3==0:
        d[n] = min(ans(n//2),ans(n//3))+1
    elif n%3==0:
        d[n] = min(ans(n//3), ans(n-1)) + 1
    elif n%2==0:
        d[n] = min(ans(n//2), ans(n-1)) + 1
    else:
        d[n] = ans(n-1) + 1
    return d[n]
print(ans(n))


# 방법3
n = int(input())
d = {1:0,2:1}
def ans(n):
    if n in d:
        return d[n]
    d[n] = min(ans(n//3)+n%3,ans(n//2)+n%2)+1
    return d[n]
print(ans(n))