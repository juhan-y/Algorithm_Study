import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

print(((a % c) * (b % c)) % c)