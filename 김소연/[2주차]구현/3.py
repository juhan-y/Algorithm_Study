import sys

n = input()

row = int(n[1])
# ascii code : 대문자 A 65, 소문자 a 97
column = int(ord(n[0])-96)

moves = [(-2,1), (-2,-1), (2,1), (2,-1), (1,-2),(1,2),(-1,2),(-1,-2)]

answer = 0

for m in moves:
    nr = row + m[0]
    nc = column + m[1]
    
    if nr >=1 and nr <= 8 and nc >=1 and nc <=8:
        answer += 1
        
print(answer)