# 삽입정렬은 2번째 index부터 시작한다. 1번째 index는 이미 정렬되어있다고 생각하기 때문

arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(arr)) :
    for j in range(i, 0, -1) :
        if arr[j] < arr[j-1] :
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else :
            break

print(arr)