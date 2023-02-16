import sys

n,m = map(int,sys.stdin.readline().split())

a,b = 1,1

# 54321 / 321 21

if n-m <= m:
    M1 = m
    M2 = n-m
else:
    M1 = n-m
    M2 = m

for i in range(2,n+1):
    
    if i <= M2:
        b *= i
    elif i > M1:
        a *= i

print(a//b)