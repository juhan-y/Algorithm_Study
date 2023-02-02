# input()으로 큰 숫자를 받으면 시간이 오래걸린다
# readline()을 사용하자

import sys

n = int(sys.stdin.readline())
my_list = []
for _ in range(n):
    my_list.append(int(sys.stdin.readline()))
my_list.sort()
for i in my_list:
    print(i)