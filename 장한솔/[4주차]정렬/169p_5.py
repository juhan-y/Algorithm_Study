array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def qs_short(array) :
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    le_array = [x for x in tail if x <= pivot]
    ri_array = [x for x in tail if x > pivot]
    
    array = qs_short(le_array) + [pivot] + qs_short(ri_array)
    return array

print(qs_short(array))