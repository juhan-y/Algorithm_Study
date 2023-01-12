n,m = map(int,input().split())
my_list = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            temp = my_list[i]+my_list[j]+my_list[k]
            if temp <= m:
                ans = max(ans,temp)
print(ans)