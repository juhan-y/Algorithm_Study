import sys

N = int(sys.stdin.readline())

house_list = []

for _ in range(N):
    house_list.append(list(map(int,sys.stdin.readline().split())))

d = [[0,0,0] for _ in range(N)]

d[0][0] = house_list[0][0]
d[0][1] = house_list[0][1]
d[0][2] = house_list[0][2]

for i in range(1,N):
    d[i][0] = min(d[i-1][1] + house_list[i][0], d[i-1][2] + house_list[i][0])
    d[i][1] = min(d[i-1][0] + house_list[i][1], d[i-1][2] + house_list[i][1])
    d[i][2] = min(d[i-1][0] + house_list[i][2], d[i-1][1] + house_list[i][2])

print(min(d[N-1]))