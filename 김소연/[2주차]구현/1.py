import sys

n = int(input())
plans = input().split()

moves = ['L', 'R', 'U', 'D']
# 좌, 우, 상, 하
dx = [0,0,-1,1]
dy = [-1,1,0,0]
x, y = 1,1

for p in plans:
    for i in range(4):
        if p == moves[i]:
           nx = x + dx[i]
           ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
