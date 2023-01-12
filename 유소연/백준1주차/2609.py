import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a1 = 0
a2 = 0

if n>m :
    n, m = m, n

for i in range(1, n+1) :
    if n%i == 0 and m%i == 0 :
        a1 = i

for j in range(n, n*m+1, n) :
    if j%m == 0 :
        a2 = j
        break

print(a1)
print(a2)
