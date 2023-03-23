def ans(n,x,y):
    global cnt
    if x > r or x + n <= r or y > c or y + n <= c:
        cnt += n**2
        return
    if n > 2:
        n//=2
        ans(n,x,y)
        






n,r,c = int(input().split())
cnt = 0
ans(2**n,0,0)
print(cnt)