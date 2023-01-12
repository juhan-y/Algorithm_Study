import sys

N = int(sys.stdin.readline())

m_list = []

for i in range(N):
    k = int(sys.stdin.readline())
    m_list.append(k)
    
m_list.sort(reverse=True)


for m in m_list:
    print(m , end=' ')
    