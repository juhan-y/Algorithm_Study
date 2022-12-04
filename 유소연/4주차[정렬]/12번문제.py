import sys

N, K = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c = 0
while True :
    if c==K :
        break
    if min(a) >= max(b) :
        break
    else :
        i =a.index(min(a))
        j =b.index(max(b))

        a[i], b[j] = b[j], a[i]
        c+=1
        
print(sum(a))

