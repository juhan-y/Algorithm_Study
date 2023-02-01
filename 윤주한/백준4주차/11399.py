n = int(input())
ls = list(map(int, input().split()))

ls.sort()
summation = 0
for i in range(n):
    summation += (n-i) * ls[i]
print(summation)