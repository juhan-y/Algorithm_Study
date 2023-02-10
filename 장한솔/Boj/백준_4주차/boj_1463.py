import sys

N = int(sys.stdin.readline())

num = [0 for _ in range(N+1)]

for i in range(2, N+1) :
    # 1 빼는 연산
    num[i] = num[i-1]+1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0 :
        num[i] = min(num[i], num[i // 2] + 1)

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0 :
        num[i] = min(num[i], num[i // 3] + 1)

print(num[N])