import sys

N = int(sys.stdin.readline())
cnt = [0, 1, 2] # n이 각각 0. 1, 2 일때 필요한 타일 개수

for i in range(3, N+1) :
    cnt.append(cnt[i-2] + cnt[i-1])

print(cnt[N] % 10007)