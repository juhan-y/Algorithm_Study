n = int(input())

target = 666
cnt = 1
while n != cnt:
    target += 1
    if '666' in str(target):
        cnt += 1

print(target)