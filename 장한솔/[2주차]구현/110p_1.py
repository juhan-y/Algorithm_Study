import sys

N = int(sys.stdin.readline())
move = list(map(str, sys.stdin.readline().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
m = ['L', 'R', 'U', 'D']

x, y = 1, 1

for i in move :
    for j in range(4) :
        if i == m[j] :
            next_x = x + dx[j]
            next_y = y + dy[j]
    if (next_x < 1) or (next_x > N) or (next_y < 1) or (next_y > N) :
        continue
    
    x = next_x
    y = next_y
    
print(x, y)

