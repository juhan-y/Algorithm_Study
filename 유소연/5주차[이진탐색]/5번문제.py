import sys

def b_search(arr, target, start, end) :
    if start > end :
        return False 
    
    mid = (start+end)//2

    if arr[mid] == target :
        return True
    elif arr[mid] > target :
        return b_search(arr, target, start, mid-1)
    else :
        return b_search(arr, target, mid+1, end)

N = int(sys.stdin.readline().rstrip())
arr_n = list(map(int, sys.stdin.readline().rstrip().split()))
arr_n = sorted(arr_n)

M = int(sys.stdin.readline().rstrip())
arr_m = list(map(int, sys.stdin.readline().rstrip().split()))

for i in arr_m :
    if b_search(arr_n ,i, 0, N) :
        print('yes')
    else :
        print('no')
    
