import sys

N,K = map(int,sys.stdin.readline().split())


lines = list(sys.stdin.readlines())

for i,line in enumerate(lines):
    lines[i] = list(map(int,line.rstrip().split()))
    lines[i].sort()
    

lines[0][:K] = lines[1][-K:]

print(sum(lines[0]))
    

    

