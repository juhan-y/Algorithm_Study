# 방법 1 : 파이썬 itertools 패키지 사용하기

from itertools import combinations
a,b = map(int, input().split())
print(len(list(combinations(range(a),b))))


# 방법 2 : 함수 만들기

#이항계수 함수
def combi(a,b):
    return factorial(a)/(factorial(b)*factorial(a-b))

# 팩토리얼 함수(재귀 함수 사용)
def factorial(n):
    if (n>1):
        return n*factorial(n-1)
    else:
        return 1

a,b = map(int, input().split())
print(int(combi(a,b)))
