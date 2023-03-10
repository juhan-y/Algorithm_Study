import sys
input = sys.stdin.readline
p = [1,1,1,2,2]
t = int(input())
for _ in range(95):
    p.append(p[-5]+p[-1])
for _ in range(t):
    n = int(input())
    print(p[n-1])
