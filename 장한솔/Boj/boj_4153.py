import sys

while(True) :
    tri_list = list(map(int, sys.stdin.readline().split()))
    tri_list.sort()
    if tri_list[0] == 0 :
        break
    if tri_list[2] * tri_list[2] == tri_list[0] * tri_list[0] + tri_list[1] * tri_list[1] :
        print('right')
    else :
        print('wrong')