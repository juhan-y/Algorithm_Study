import sys
import math
from itertools import permutations

N = int(sys.stdin.readline())

map_list = []

for _ in range(N):
    map_list.append(list(map(int,sys.stdin.readline().split())))

N_cnt = int(math.log2(N))
ans = [0,0]

for k in range(N_cnt+1): # 자를 횟수

    pos = N//pow(2,k) # 8//2^0 = 8 , 8//2^1 = 4, 8//2^2 = 2, 8//2^3 = 1
    x_list = []
    y_list = []

    for i in range(N//pow(2,N_cnt - k)): #  8//2^(3-0) = 1, 8//2^(3-1) = 2 , 4, 8
        x_list.append(i * pos)
        y_list.append(i * pos)
    
    for x in x_list:
        for y in y_list:
            flag = False
            for n in range(pos):

                tmp = map_list[y+n][x:x+pos] # 가로 방향

                if max(tmp) == min(tmp) and min(tmp) <= 1:
                    pass
                else:
                    flag = True
                    break     
                
                tmp.clear()
                for z in range(pos): # 세로 방향
                    tmp.append(map_list[y+z][x+n])

                if max(tmp) == min(tmp) and min(tmp) <= 1:
                    pass
                else:
                    flag = True
                    break  
        
            if flag == False:
                ans[max(tmp)] += 1
                for n in range(pos):
                    map_list[y+n][x:x+pos] = [2] * pos


for a in ans:
    print(a)
    
    
    
    


        

    
