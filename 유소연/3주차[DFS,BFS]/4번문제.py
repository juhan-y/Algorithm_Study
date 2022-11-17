def recur(i) :
    if i==10 :
        return
    
    print(i, '번째 재귀 함수에서', i+1,'번째 재귀 함수를 호출합니다.')

    recur(i+1)
    print(i,'번째 재귀함수를 종료합니다')

recur(1)