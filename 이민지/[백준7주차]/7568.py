import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    l.append(input().split())
for x,y in l:
    rank = 1
    for w,h in l:
        if int(x)<int(w) and int(y)<int(h):
            rank += 1
    print(rank, end=' ')