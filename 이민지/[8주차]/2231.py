# 유식한 for문 풀이
N = int(input())
ans = 0
for i in range(max(0,N-len(str(N))*9),N):
    if sum(map(int,str(i))) +i == N:
        ans = i
        break
print(ans)
        

# 무식한 for문 풀이
# num = int(input())
# min_val = 0
# for a in range(9,-1,-1):
#     for b in range(9,-1,-1):
#         for c in range(9,-1,-1):
#             for d in range(9,-1,-1):
#                 for e in range(9,-1,-1):
#                     for f in range(9,-1,-1):
#                         val = a*100000+b*10000+c*1000+d*100+e*10+f
#                         temp = val+(a+b+c+d+e+f)
#                         if (temp==num):
#                             min_val = val
# print(min_val)
            
    