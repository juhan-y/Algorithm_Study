def fac_iter(n) :
    result = 1
    for i in range(1, n+1) : # 1부터 n까지 차례대로 곱하기
        result *= i
    return result 

def fac_rec(n) :
    if n <= 1 : # 0!이나 1!은 모두 1이기 때문에, 종료조건을 명시한 것
        return 1
    
    return n * fac_rec(n-1) # n * (n-1)! = n! 라는 것을 재귀함수를 통해 구현