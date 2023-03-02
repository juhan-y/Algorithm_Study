t = int(input())
l = [[0] * (15) for _ in range(15)]
for i in range(15):
    l[0][i] = i
for i in range(1,15):
    for j in range(1,15):
        for k in range(1,j+1):
            l[i][j] += l[i-1][k]
for _ in range(t):
    k = int(input())
    n = int(input())
    print(l[k][n])