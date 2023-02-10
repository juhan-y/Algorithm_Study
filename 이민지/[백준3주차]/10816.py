# 방법1: 이분탐색

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
cnt = {}

def binary(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if target == n_list[mid]:
            return cnt.get(target)
        if target < n_list[mid]:
            right = mid - 1
        if target > n_list[mid]:
            left = mid + 1
    return 0

for i in n_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in m_list:
    print(binary(i), end=' ')

# 방법2: counter 함수

import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

C = Counter(n_list)

for i in m_list:
    if i in C:
        print(C[i], end=' ')
    else:
        print(0, end=' ')

# 방법3: 해쉬 알고리즘

import sys
n = int(sys.)
