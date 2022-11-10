# 재귀 종료
import sys

def re_f(i):
    if i == 10:
        return
    print(i, '번째 재귀에서', i+1, '번째 재귀함수 호출')
    re_f(i+1)
    print(i, '번째 재귀함수 종료')
    
re_f(1)