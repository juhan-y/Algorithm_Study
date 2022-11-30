array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def qs(array, start, end) :
    if start >= end :
        return array
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right :
        # left는 pivot보다 큰 값을, right는 pivot보다 작은 값을 찾는 것이 목표!!
        while (left <= end) and (array[left] <= array[pivot]) :
            left += 1
        while (right > start) and (array[right] >= array[pivot]) :
            right -= 1
            
        if right >= left :
            array[right], array[left] = array[left], array[right]
        else :
            array[right], array[pivot] = array[pivot], array[right]
        
    qs(array, start, right-1)
    qs(array, right+1, end)            

qs(array, 0, len(array)-1)
print(array)