def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

N = int(input())
array1 = list(map(int, input().split()))
array1.sort()

M = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    result = binary_search(array1, i, 0, N - 1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')
