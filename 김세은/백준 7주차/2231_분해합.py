# 2231 분해합
N = int(input())

for i in range(1, N+1):
    a = list(map(int, str(i)))
    ans = i + sum(a)
    if ans == N:
        print(i)
        break

    elif i == N:
        print(0)
