# 가장 큰 데이터와 가장 작은 데이터의 차이가 1000000을 넘지 않을 때 효과적으로 사용 가능
# 크기가 max(array)인 array를 선언하고, 해당 값의 index를 1증가시키는 방식으로 정렬

arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(arr)+1)

for i in range(len(arr)) :
    count[arr[i]] +=1 


for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end=' ')