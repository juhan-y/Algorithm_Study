# 방법1 : 가장 빠름 40ms
n = int(input())
for i in range(max(0,n-len(str(n))*9),n):
    if sum(map(int,str(i))) + i == n:
        print(i)
        break
else:
    print(0)

# 방법2 : 메모리도 많이 잡아먹고 시간도 오래 걸림 1232ms
ans = [0] * (1000001)
for i in range(1000001):
    if ans[i] == 0:
        ans[i] = sum(map(int,str(i))) + i
n = int(input())
print(ans.index(n) if n in ans else 0)

# 방법3 : 576ms
num = int(input())
min_val = 0
for a in range(9,-1,-1):
    for b in range(9,-1,-1):
        for c in range(9,-1,-1):
            for d in range(9,-1,-1):
                for e in range(9,-1,-1):
                    for f in range(9,-1,-1):
                        val = a*100000+b*10000+c*1000+d*100+e*10+f
                        temp = val+(a+b+c+d+e+f)
                        if (temp==num):
                            min_val = val
print(min_val)