# 11055_가장 큰 증가하는 부분 수열
N = int(input())
S = list(map(int, input().split()))
li = S[:]

for i in range(N):
    for j in range(i):
        if S[j] < S[i]:
            li[i] = max(li[i], li[j]+S[i])

print(max(li))
