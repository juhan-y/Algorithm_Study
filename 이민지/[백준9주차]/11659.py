import sys
input = sys.stdin.readline
n,m = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n-1):
    l[i+1] += l[i]
l = [0] + l
for _ in range(m):
    i,j = map(int, input().split())
    print(l[j]-l[i-1])