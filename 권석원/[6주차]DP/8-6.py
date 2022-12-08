import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

ans = []

for i in range(n//2):
    tmp = 0
    jump = True
    for j in range(i,n):
        if jump:
            tmp += lst[j]
            jump = False
        else:
            jump = True
    
    ans.append(tmp)

print(max(ans))
    