n = int(input())
ls = list(input().split())
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
graph = [[1] * n for _ in range(n)]

ci, cj = 0, 0
direction = []
for i in ls:
    if i == 'R':
        direction.append(0)
    elif i == 'D':
        direction.append(1)
    elif i == 'L':
        direction.append(2)
    elif i == 'U':
        direction.append(3)    
for k in direction:
    ni = ci + di[k]
    nj = cj + dj[k]
    if 0 <= ni < n and 0 <= nj < n:
        ci, cj = ni, nj

print(nj+1, ni+1)