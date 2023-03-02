a,b = 1,1
n = int(input())
my_list = list(input().split())
for i in my_list:
    if i=='D':
        if a!=n:
            a+=1
    if i=='U':
        if a!=1:
            a-=1
    if i=='L':
        if b!=1:
            b-=1
    if i=='R':
        if b!=n:
            b+=1
print(a, b)
