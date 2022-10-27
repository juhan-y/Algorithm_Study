N, M = map(int, input().split())
ans = []

for _ in range(N):
    ls = list(map(int, input().split()))
    ans.append(min(ls))
print(max(ans))