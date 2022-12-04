import sys

def b_search(arr, target, start, end) :
    if start>end :
        return False
    mid = (start+end)//2
    temp = 0
    for i in arr :
        if i>mid : 
            temp += i-mid
    
    if temp == target :
        return mid
    elif temp < target :
        return b_search(arr, target, start, mid-1)
    else :
        return b_search(arr, target, mid+1, end)

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr = sorted(arr)
# h는 arr의 가장 큰 값보다 작아야함

print(b_search(arr, M, 0, max(arr)))

