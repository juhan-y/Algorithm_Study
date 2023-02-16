import sys

N = int(sys.stdin.readline())

tri_list = []
d = []

for _ in range(N):
    tri_list.append(list(map(int,sys.stdin.readline().split())))
    d.append([0]*(N))

d[0][0] = tri_list[0][0]

for i in range(1,N):
    for j in range(0,i+1):
        if j-1 == -1:
            d[i][j] = max(d[i-1][j] + tri_list[i][j], d[i][j])
        else:
            d[i][j] = max(d[i-1][j-1] + tri_list[i][j], d[i][j])
            d[i][j] = max(d[i-1][j] + tri_list[i][j], d[i][j])

print(max(d[N-1]))

