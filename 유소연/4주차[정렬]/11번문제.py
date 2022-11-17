import sys

n = int(sys.stdin.readline())
arr = {}

for i in range(n) :
    temp = sys.stdin.readline().split()
    arr[temp[0]] = temp[1]

arr = sorted(arr.items(), key=lambda x:x[1])

for i in arr :
    print(i[0], end=' ')