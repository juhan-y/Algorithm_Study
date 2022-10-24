n = 1260
ls = [500,100,50,10]
cnt = 0
for i in ls:
    cnt += (n//i)
    n %= i
    
print(cnt)