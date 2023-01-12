INF = int(1e10)
n = int(input())-1
for i in range(INF):
    n-=i*6
    if n <=0:
        print(i+1)
        break
    