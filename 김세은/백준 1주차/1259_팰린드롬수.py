# 1259 팰린드롬수
while True:
    N = input()
    if N=='0':
        break

    if N==N[::-1]:
        print('yes')
    else:
        print('no')
