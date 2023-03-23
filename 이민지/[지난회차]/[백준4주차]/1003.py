T = int(input())
d = [[0] *2 for _ in range(41)]
d[0] = [1,0]
d[1] = [0,1]
for v in range(2,41):
    d[v][0] += (d[v-1][0]+d[v-2][0])
    d[v][1] += (d[v-1][1]+d[v-2][1])
for _ in range(T):
    n = int(input())
    print(d[n][0], d[n][1])
