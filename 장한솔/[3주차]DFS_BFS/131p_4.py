def recur_fin_test(i) :
    if i == 100 : # 재귀함수의 종료조건 명시
        return 
    
    print(i, "번째 재귀에서", i+1, "번째 재귀 호출")
    recur_fin_test(i+1)
    print(i, "번째 재귀 종료")
    
recur_fin_test(1)