# 예제 4-2
N = int(input())
cnt = 0

for i in range(N+1):
    for j in range(0, 60):
        for k in range(0, 60):
            if str(N) in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
