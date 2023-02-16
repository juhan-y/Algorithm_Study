# 1931 회의실 배정
import sys

N = int(input())

li = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    li.append(a)
    
li = sorted(li, key=lambda x: x[0]) # 시작 시간 기준 오름차순
li = sorted(li, key=lambda x: x[1]) # 끝나는 시간 기준 오름차순

end = 0
cnt = 0

for i in range(N):
    if end <= li[i][0]:
        cnt += 1
        end = li[i][1]
        
print(cnt)
