import sys

L = int(sys.stdin.readline())
st = sys.stdin.readline().strip()
answer = 0

for i in range(L) :
    answer += (ord(st[i]) - 96) * (31 ** i) # 소문자 아스키코드 97 ~ 122
    answer = answer % 1234567891

print(answer)