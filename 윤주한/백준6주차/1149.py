n = int(input())

color = []

for _ in range(n):
    color.append(list(map(int, input().split())))

INF = int(1e9)
d = [[INF] * 3 for _ in range(n)]

d[0][0] = color[0][0]
d[0][1] = color[0][1]
d[0][2] = color[0][2]

for i in range(1, n):
    d[i][0] = min(d[i][0], d[i-1][1] + color[i][0], d[i-1][2] + color[i][0])
    d[i][1] = min(d[i][1], d[i-1][0] + color[i][1], d[i-1][2] + color[i][1])
    d[i][2] = min(d[i][2], d[i-1][0] + color[i][2], d[i-1][1] + color[i][2])

print(min(d[n-1]))