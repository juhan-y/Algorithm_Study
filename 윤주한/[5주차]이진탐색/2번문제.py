n, target = map(int, input().split())

ls = list(map(int, input().split()))

start = 0
end = len(ls) - 1
result = None
while start <= end:
    mid = (start + end) // 2
    if ls[mid] == target:
        result = mid
        break
    elif ls[mid] > target:
        end = mid - 1
    elif ls[mid] < target:
        start = mid + 1
    
if not result:
    print("원소가 존재하지 않습니다.")
else:
    print(mid+1)