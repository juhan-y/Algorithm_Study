import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    x,y=map(int,input().split())
    l.append([y,x])
l.sort()
for i,j in l:
    print(j, i)