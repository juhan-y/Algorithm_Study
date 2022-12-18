n, k = map(int, input().split())
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
ls1.sort()
ls2.sort(reverse=True)

for i in range(k):
    if ls2[i] > ls1[i]:
        ls1[i], ls2[i] = ls2[i], ls1[i]

print(sum(ls1))