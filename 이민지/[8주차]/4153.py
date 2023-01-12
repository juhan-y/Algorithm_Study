# sorted 함수는 정렬된 리스트를 리턴해주지만 sort 함수는 아무것도 리턴해주지 않는다.
my_list = []
while (my_list !=[0,0,0]):
    my_list = sorted(list(map(int,input().split())))
    if (my_list == [0,0,0]):
        break
    if ((my_list[0]**2)+(my_list[1]**2)==(my_list[2]**2)):
        print("right")
    else:
        print("wrong")
    