n,m = map(int, input().split())
ans = 0
for i in range(n):
    my_list=list(map(int,input().split()))
    ans = max(ans,min(my_list))
print(ans)
