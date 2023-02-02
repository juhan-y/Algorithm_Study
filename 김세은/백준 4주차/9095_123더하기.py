# 9095 1,2,3 더하기
import sys
T = int(input())

d = [0]*11

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = sum(d[i-3:i])

for i in range(T):
    n = int(sys.stdin.readline())
    print(d[n])




'''
1




(1)+1

2




(1)+2

(1+1)+1
(2)+1

3




(1)+3

(1+1)+2
(2)+2

(1+2)+1
(1+1+1)+1
(2+1)+1
(3)+1
'''
