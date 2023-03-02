# 냅색 알고리즘 (추후정리)
import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])





# 이 문제는 NP-hard이기 때문에 그리디 알고리즘으로는 풀 수 없다.
# 반례
# 4 9
# 1 101
# 8 100
# 4 51
# 4 51
# 정답 : 203
# 출력 : 201

n,k = map(int,input().split())
l = []
for _ in range(n):
    w,v = map(int,input().split())
    l.append([w,v])
l.sort(reverse = True, key = lambda x:x[1])
ans = 0
for i in range(len(l)):
    val = 0
    cnt = 0
    for w,v in l[i-1:]:
        if cnt+w <= k:
            cnt += w
            val += v
    if val > ans:
        ans = val
print(ans)


