# 실전) 1이 될때까지
# 수 n이 1이 될때까지 
#  1. n -= 1
#  2. n /= k (n/k ==0 일때만) => 나누기 최우선

import sys

n, k = map(int, input().split())
count =0

while n:
    if n == 1:
        break
    if n%k ==0:
        n /= k
        count +=1
    else:
        n -= 1
        count +=1

print(count)