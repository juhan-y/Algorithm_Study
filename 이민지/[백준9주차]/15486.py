import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
d = [0]*(n+1)
x = 0
for i in range(n):
    x = max(d[i],x)
    if l[i][0]+i<=n:
        d[l[i][0]+i] = max(x+l[i][1], d[l[i][0]+i])
print(max(d))


        # # 시간초과
        # import sys
        # input = sys.stdin.readline
        # n = int(input())
        # l = []
        # for _ in range(n):
        #     l.append(list(map(int,input().split())))
        # d = [0]*n
        # d[0] = l[0][1]
        # for i in range(n):
        #     if l[i][0]+i>n:
        #         continue
        #     for j in range(i):
        #         if l[j][0]+j>i:
        #             continue
        #         d[i] = max(d[i],d[j]+l[i][1]) 
        # print(max(d))