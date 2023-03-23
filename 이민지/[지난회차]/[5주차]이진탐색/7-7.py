# 집합 자료형
# set() 함수 이용
# set은 인덱스도 순서도 없기 때문에 list보다 데이터 찾는 속도가 빠르다

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')