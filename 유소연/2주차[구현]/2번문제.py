import sys

N = sys.stdin.readline()
N = int(N)
count = 0
n_answer = [3,13,23]
answer = [3,13,23,30,33,43,53]

for i in range(N+1) :
    for j in range(60) :
        for k in range(60) :
            if i in n_answer :
                count +=1
            elif j in answer :
                count +=1
            elif k in answer :
                count +=1
            
print(count)
