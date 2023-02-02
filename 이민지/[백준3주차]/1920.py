# for문을 쓰면 시간초과가 된다
# 이분탐색을 사용하자

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if target == n_list[mid]:
            return True
        if target < n_list[mid]:
            right = mid - 1
        if target > n_list[mid]:
            left = mid + 1

for i in range(m):
    if binary(targets[i]):
        print(1)
    else:
        print(0)