# list.index(i)의 시간복잡도는 O(N)
# 딕셔너리를 쓰자

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list((set(arr))))
ans = {}
for i in range(len(arr2)):
    ans[arr2[i]] = i

for i in arr:
    print(ans[i], end = ' ')