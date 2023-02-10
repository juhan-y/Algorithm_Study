import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))

temp = sorted(set(ls))
for i in ls:
    print(bisect_left(temp, i), end=' ')