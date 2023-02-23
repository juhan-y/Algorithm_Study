# 7568 덩치
import sys

N = int(input())

li = []
ans = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

for i in range(N):
    cnt = 1
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    ans.append(cnt)

for i in ans:
    print(i, end=' ')
