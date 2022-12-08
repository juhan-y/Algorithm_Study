"""
1. 점화식 만들기
2. 초기항 생각하기
"""

n = int(input())
l = list(map(int, input().split()))
d = [0] * (n+1)
d[0] = l[0]
d[1] = max(l[0],l[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+l[i])

print(d[n-1])