def recur(count) :
    if count == 5 :
        return
    print('재귀함수 호출')
    count+=1
    recur(count)

recur(0)