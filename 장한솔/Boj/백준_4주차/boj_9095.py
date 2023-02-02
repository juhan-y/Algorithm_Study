import sys

T = int(sys.stdin.readline())
cnt = [0] * 12
cnt[1] = 1
cnt[2] = 2
cnt[3] = 4

for i in range(4, 12) :
    cnt[i] = cnt[i-3] + cnt[i-2] + cnt[i-1]

for _ in range(T) :
    n = int(sys.stdin.readline())
    print(cnt[n])