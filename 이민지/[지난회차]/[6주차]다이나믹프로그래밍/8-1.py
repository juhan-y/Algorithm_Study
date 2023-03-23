# 피보나치함수를 재귀함수로 구현
# 단점 시간복잡도가 O(2^n)이라서 n이 커지면 계산할 수 없다
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))