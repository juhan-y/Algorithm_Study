# 10250 ACM호텔
import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    a = N//H
    b = N%H
    ans = (100*b) + (a+1)
    if N%H == 0:
        b = H
        ans = (100*H) + a
    print(ans)
