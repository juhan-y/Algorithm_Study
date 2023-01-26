# 10816 숫자 카드2
import sys
from collections import Counter

N = int(input())
li1 = list(map(int, sys.stdin.readline().split()))

M = int(input())
li2 = list(map(int, sys.stdin.readline().split()))

c = Counter(li1)

for i in range(len(li2)):
    if li2[i] in c:
        print(c[li2[i]], end=' ')
    else:
        print(0, end=' ')
