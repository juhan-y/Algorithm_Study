import sys

N,M,K = map(int,sys.stdin.readline().rstrip().split())

lst = list(map(int,sys.stdin.readline().rstrip().split()))
lst.sort(reverse=True)

cnt = [0] * N
pos = 0
ans = 0

for i in range(M):
    
    for j in range(pos):
        if cnt[j] == 0:
            cnt[pos] = 0
            pos = j         
            break
    
    if cnt[pos] >= K:
        cnt[pos] = 0
        if pos > 0:
            pos -=1
        else :
            pos +=1
           
    cnt[pos] += 1        
    ans += lst[pos]
    

print(ans)