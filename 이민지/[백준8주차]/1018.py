n,m = map(int,input().split())
l = []
cnt = []
for _ in range(n):
    l.append(input())
for i in range(n-7):
    for j in range(m-7):
        p,q = 0,0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0:
                    if l[x][y] == 'W':
                        p += 1
                    if l[x][y] == 'B':
                        q += 1
                else:
                    if l[x][y] == 'B':
                        p += 1
                    if l[x][y] == 'W':
                        q += 1
        cnt.append(min(p,q))
print(min(cnt))

