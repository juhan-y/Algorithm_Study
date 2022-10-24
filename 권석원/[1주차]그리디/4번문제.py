import sys

N,K = map(int,sys.stdin.readline().rstrip().split())

ans = 0
sum = N

while sum > 1:   
    if sum % K == 0:
        sum = min(sum - 1,sum//K)
    else:
        sum -= 1
        
    ans +=1
    
print(ans)
    