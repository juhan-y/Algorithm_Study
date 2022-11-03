import sys

N = sys.stdin.readline().strip()
c = int(ord(N[0]))
r = int(N[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result = 0
for s in steps :
    next_r = r + s[0]
    next_c = c + s[1]
    
    if (next_r >= 1) and (next_r <= 8) and (next_c >= 1+ord('a')) and (next_c <= 8+ord('a')) :
        result += 1

print(result)