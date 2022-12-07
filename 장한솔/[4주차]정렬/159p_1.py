array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

leng = len(array)
for i in range(leng) :
    min_index = i
    for j in range(i+1, leng) :
        if array[j] > array[i] :
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

print(array)

## swap

# k = array[i]
# array[i] = array[min_index]
# array[min_index] = k