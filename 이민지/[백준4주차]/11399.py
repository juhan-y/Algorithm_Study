n = int(input())
arr = sorted(list(map(int,input().split())), reverse=True)
ans = 0
for i in range(n):
    ans += (i+1)*arr[i]
print(ans)
