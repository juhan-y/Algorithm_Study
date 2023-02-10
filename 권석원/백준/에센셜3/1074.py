import sys

N,r,c = map(int,sys.stdin.readline().split())

def z(n,num,x,y,N):
    next_n = n//2
    
    if y == r and x == c:
        print(num)
        return

    if x <= c and y <= r and x + next_n-1 >= c and y + next_n-1 >= r:
        z(next_n, num, x, y, N-1)
    elif x + next_n <= c and y <= r and x + (next_n*2)-1 >= c and y + next_n-1 >= r:
        z(next_n, num + pow(2,2*(N-1)), x + next_n, y, N-1)
    elif x <= c and y + next_n <= r and x + next_n-1 >= c and y + (next_n*2)-1 >= r:
        z(next_n,num + pow(2,2*(N-1)+1), x, y + next_n, N-1)
    elif x + next_n <= c and y + next_n <= r and x + (next_n*2)-1 >= c and y + (next_n*2)-1 >= r:
        z(next_n, num + pow(2,2*(N-1))*3, x + next_n, y + next_n, N-1)

z(pow(2,N),0,0,0,N)

# num = 0

# def z(n,x,y):
#     global num

#     next_n = n//2

#     if n == 1:
#         if y == r and x == c:
#             print(num)
#         else:
#             num += 1
#     else: 
#         z(next_n,x,y)
#         z(next_n,x + next_n,y)
#         z(next_n,x ,y + next_n)
#         z(next_n,x + next_n ,y + next_n)

# z(pow(2,N),0,0) 

# 시작과 num 값을 r과 c에서 시작하도록 만들면 되는거 아님?