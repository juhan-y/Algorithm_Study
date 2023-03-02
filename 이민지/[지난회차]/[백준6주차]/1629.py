# 분할정복
import sys
input = sys.stdin.readline
def P(C,n):
    if n==1:
        return C%c
    if n%2:
        y = P(C,(n-1)/2)
        return (y*y*C)%c
    else:
        y = P(C,(n/2))
        return (y*y)%c
   
a,b,c = map(int,input().split())
print(P(a,b))
