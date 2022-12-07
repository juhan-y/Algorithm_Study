array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

leng = len(array)
for i in range(1, leng) :
    # i번째 데이터를 왼쪽으로 이동하면서 비교해야되기 때문에 range(i, 0, -1)
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break

print(array)