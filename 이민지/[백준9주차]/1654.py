# 이분탐색
k,n = map(int,input().split())
l = []
for _ in range(k):
    l.append(int(input()))
start, end = 1, max(l)
ans = 0
while(start<=end):
    cnt = 0
    mid = (start+end)//2
    for i in l:
        cnt += i//mid
    if cnt < n:
        end = mid -1
    else:
        ans = mid
        start = mid + 1
print(ans)

