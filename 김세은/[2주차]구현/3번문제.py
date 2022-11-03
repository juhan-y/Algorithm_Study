# 4-3번 문제
n = list(input())

x, y = ord(n[0]) - 96, int(n[1])
cnt = 0

#(-2, -1) (-2, 1) (2, -1) (2, 1) (1, -2) (1, 2) (-1, -2) (-1, 2)

dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    cnt += 1
print(cnt)
