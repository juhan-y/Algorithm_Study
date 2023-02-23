# ord 함수, enumerate 함수 사용

# 방법1
l = input()
s = input()
ans = 0
r = 1
m = 1234567891
for i in s:
    ans += (ord(i)-96)*r % m
    r *= 31
print(ans%m)



# 방법2 파이썬답게 풀기
input()
print(sum((ord(n)-96)*31**m for m,n in enumerate(input()))%1234567891)