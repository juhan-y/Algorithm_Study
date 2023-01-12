import sys

while True:
    string = sys.stdin.readline().rstrip()

    if string == '0':
        break
    
    len_str = len(string)
    front = string[:len(string)//2]
    
    if len_str %2: # 홀수
        back = string[len(string)//2 +1:]
    else: # 짝수
        back = string[len(string)//2:]

    if front == back[::-1]:
        print('yes')
    else:
        print('no')