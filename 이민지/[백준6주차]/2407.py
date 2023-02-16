import sys
from math import factorial
input = sys.stdin.readline
n,m = map(int, input().split())
x = factorial(n)
y = factorial(n-m)*factorial(m)
print(x//y)