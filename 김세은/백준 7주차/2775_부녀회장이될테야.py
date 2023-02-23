# 2775 부녀회장이 될테야
import sys

T = int(input())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    li = [i for i in range(1, n+1)]

    for j in range(1, k+1):
        for a in range(1, n):
            li[a] += li[a-1]
            
    print(li[n-1])
