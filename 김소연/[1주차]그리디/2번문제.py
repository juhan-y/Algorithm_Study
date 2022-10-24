# 실전) 큰수의 법칙
# n개의 수 m번 더하기, 단 같은수 k번까지만 반복 가능

import sys

n,m,k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
answer = 0

def check_m(m):
    if m == 0:
        return 1
    
while m:
    for i in range(k):
        answer += nums[-1]
        m -= 1
        if check_m(m) ==1: break

    answer += nums[-2]
    m -= 1
    
    if check_m(m) ==1: break

print(answer)


## 실전) 큰수의 법칙

# n,m,k = map(int, input().split())
# nums = list(map(int, input().split()))

# nums.sort()
# f = nums[-1]
# s = nums[-2]
# answer = 0

# count_1 = m/(k+1)
# count_2 = m%(k+1)

# answer += count_1 * (f*k + s)
# answer += count_2 * f

# print(int(answer))