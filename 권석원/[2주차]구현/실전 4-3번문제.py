import sys

pos = sys.stdin.readline().rstrip()

col = pos[0]
row = pos[1]

col = ord(col) - ord('a')
row = int(row)-1

dx = [2,-2,-1,1,2,-2,-1,1]
dy = [1,1,2,2,-1,-1,-2,-2]

cnt = 0

for i in range(8):
    nx = col + dx[i]
    ny = row + dy[i]
    
    if 0 > nx and nx <= 8: continue
    if 0 > ny and ny <= 8: continue
    
    cnt += 1
    

print(cnt)
    