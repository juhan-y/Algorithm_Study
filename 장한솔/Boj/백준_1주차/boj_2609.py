import sys
import math

A, B = map(int, sys.stdin.readline().split())
GCD = math.gcd(A, B)

print(math.gcd(A, B))
print(GCD * (A // GCD) * (B // GCD))