import sys
N = int(sys.stdin.readline())

N += 1

if 13 <= N < 23:
    k = 2
elif 3 <= N < 13:
    k = 1
elif N < 3:
    k = 0
else :
    k = 3

res = 60*60*k 
res += ((15 * 45) + (60 * 15) ) * (N-k)   

print(res)