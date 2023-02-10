## https://pacific-ocean.tistory.com/192
d = [0] * 11
t = int(input())
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7
d[5] = 13

# 1 

# 1 1 
# 2 

# 1 1 1 
# 2 1 
# 1 2 
# 3 

# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2
# 1 3
# 3 1

# 1 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 2 1 1
# 2 1 1 1
# 1 2 2
# 2 1 2
# 2 2 1
# 1 1 3
# 1 3 1
# 3 1 1
# 2 3
# 3 2


for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(t):
    print(d[int(input())])
