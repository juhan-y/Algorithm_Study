import sys

while True:
    input_list = list(map(int,sys.stdin.readline().split()))
    
    if input_list[0] == 0 and input_list[1] == 0 and input_list[2] == 0:
        break
    
    max_val = max(input_list)
    input_list.remove(max_val)

    comp_val = 0

    for i in input_list:
        comp_val += i*i

    if max_val*max_val == comp_val:
        print('right')
    else:
        print('wrong')
