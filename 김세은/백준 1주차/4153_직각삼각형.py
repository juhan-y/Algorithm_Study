# 4153 직각삼각형
while True:
    li = list(map(int, input().split()))
    max_li = max(li)
    if sum(li)==0:
        break
    li.remove(max_li)

    if (li[0]*li[0]) + (li[1]*li[1]) == (max_li*max_li):
        print('right')
    else:
        print('wrong')
