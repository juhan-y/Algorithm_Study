n = int(input())
arr = []
ans = 0
end = 0
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr = sorted(arr, key=lambda x:(x[1],x[0]))
for s, e in arr:
    if s >= end:
        ans += 1
        end = e
print(ans)
               