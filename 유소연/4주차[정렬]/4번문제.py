# 정렬시 왼쪽에있는 리스트는 pivot보다 작고, 오른쪽에 있는 리스트는 pivot보다 크다는 특징을 이용

arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end) :
    if start >= end :
        return
    
    pivot = start
    left = start+1
    right = end

    while left <= right : #왼쪽은 pivot보다 큰 데이터를 찾는다(큰 데이터를 오른쪽으로 넘겨야하기 때문)
        while left <= end and arr[left] <= arr[pivot] :
            left +=1
        
        while right > start and arr[right] >= arr[pivot] : #오른쪽은 pivot보다 작은 데이터를 찾는다
            right +=1

        if left>right : 
            arr[right], arr[pivot] = arr[pivot], arr[right] # pivot왼쪽으로 pivot보다 작은 수를 정렬하기 위함
        else :
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)