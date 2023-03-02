#유클리드 호제법
a,b = map(int,input().split())

#최대공약수
# 'a'와 'b'의 최대 공약수는 'b'와 'a를 b로 나눈 나머지'의 최대 공약수 
def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a
     
# 최소공배수
# 'a'와 'b'의 곱을 'a'와 'b'의 최대 공약수로 나눈 값
def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))

# a,b = map(int,input().split())
# n=max(a,b)
# m=1
# while True:
#     if a%n==0 and b%n==0:
#         print(n)
#         break
#     n-=1
    
# while True:
#     if m%a==0 and m%b==0:
#         print(m)
#         break
#     m+=1