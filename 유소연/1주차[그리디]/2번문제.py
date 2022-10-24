from re import L
import sys

n, m, k =  map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
asw = 0
arr.sort(reverse=True)

for i in range(1, m+1) :
    if i % (k+1) == 0 :
        asw += arr[1]
    else :
        asw += arr[0]
print(asw)