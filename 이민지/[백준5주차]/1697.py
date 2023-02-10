# 방법1 : 재귀
# 탑다운방식, 동생이 수빈이에게 간다고 생각하자
def ans(n,k):
    if n >= k:
        return n-k
    elif k == 1: # 예외처리
        return 1
    elif (k%2==0):
        return min(k-n, ans(n,k//2)+1)
    elif (k%2==1):
        return min(ans(n,k-1),ans(n,k+1))+1
        
n, k = map(int, input().split())
print(ans(n,k))