import sys

N = sys.stdin.readline()
arr = []

for i in range(int(N)) :
    temp = sys.stdin.readline()
    arr.append(int(temp))

arr = sorted(arr, reverse=True)
print(arr)
