import sys

N = int(sys.stdin.readline())

mr_list = []

for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    c = b - a
    mr_list.append((a,b,c))

mr_list.sort()

#mr_list.sort(key= lambda x : (x[0],x[2]))


pre_a, pre_b, pre_c = -1,-1,-1
ans = 0

for abc in mr_list:
    a,b,c = abc

    if a == b:
        pre_a,pre_b = a,b
        ans += 1
        continue

    if (pre_a <= a and pre_b >= b) or pre_a >= b:
        pre_a,pre_b = a,b
    else:
        #회의 추가
        if pre_b <= a and pre_b <= b:
            pre_a,pre_b = a,b
            ans += 1
        #넘김

print(ans)