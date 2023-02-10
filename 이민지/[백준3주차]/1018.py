n,m = map(int, input().split())
pan = []
cnt = []

for _ in range(n):
    pan.append(input())

for x in range(n-7):
    for y in range(m-7):
        index1 = 0
        index2 = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if ( i + j ) % 2==0:
                    if pan[i][j]=='B':
                        index1 += 1
                    if pan[i][j]=='W':
                        index2 += 1
                else:
                    if pan[i][j]=='W':
                        index1 += 1
                    if pan[i][j]=='B':
                        index2 += 1
        cnt.append(index1)
        cnt.append(index2)
print(min(cnt))

