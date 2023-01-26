# 1920 수 찾기
import sys

N = int(input())
li1 = set(map(int, sys.stdin.readline().split()))

M = int(input())
li2 = list(map(int, sys.stdin.readline().split()))

for i in li2:
    if i in li1:
        print(1)
    else:
        print(0)
