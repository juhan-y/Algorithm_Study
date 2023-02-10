# 2609 최대공약수와 최소공배수
import sys

a, b = map(int, sys.stdin.readline().split())

n, m = a, b

while m!=0:
    n, m = m, n % m

print(n)
print((a*b)//n)
