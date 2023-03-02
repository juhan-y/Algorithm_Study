
# 추후정리
import sys

S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])



# 안됨
import sys
from itertools import combinations
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
result = []
for i in range(1,len(a)+1):
    result = result + list(combinations(a,i))
for i in result:
    for j in i:
        