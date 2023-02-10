n = int(input())
my_list = list(map(int,input().split()))
cnt = 0

# 소수판별함수
def isprime(a):
    if a==1:
        return False
    if a==2:
        return True
    b = int(a**(1/2))+1
    for i in range(2,b):
        if a%i==0:
            return False
    return True

for i in my_list:
    if isprime(i)==True:
        cnt+=1
print(cnt)


