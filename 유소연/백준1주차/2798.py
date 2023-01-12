import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            temp = arr[i]+arr[j]+arr[k]
            if result < temp and temp <= m :
                result = temp

print(result)