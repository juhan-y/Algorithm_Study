# 스택
# First in Last Out
# 삽입 5,2,3,7 -> 삭제 -> 삽입 1, 4 -> 삭제
import sys

s = []
s.append(5)
s.append(2)
s.append(3)
s.append(7)
s.pop()
s.append(1)
s.append(4)
s.pop()

#제일 안쪽 부터
print(s)
#제일 위 부터
print(s[::-1])

