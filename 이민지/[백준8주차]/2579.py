n = int(input())
l = [0] * n
ans = [0] * n
for i in range(n):
    l[i] = int(input())
if n==1:
    print(l[0])
if n==2:
    print(l[0]+l[1])
if n>=3:
    ans[0] = l[0]
    ans[1] = l[0]+l[1]
    ans[2] = max(l[0],l[1])+l[2]
    for i in range(3,n):
        ans[i] = max(l[i-1]+ans[i-3], ans[i-2]) + l[i]
    print(ans[n-1])
