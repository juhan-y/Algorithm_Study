n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target_ls = list(map(int, input().split()))
arr.sort()
def binary_search(target, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 'yes'
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

for target in target_ls:
    print(binary_search(target, arr), end = ' ')