n = input()
dic = {'a':0, 'b':1, 'c':2, 'd': 3, 'e': 4, 'f':5, 'g': 6, 'h':7}
j = dic[n[0]]
i = int(n[1]) - 1

dj = [1, 2, 1, 2, -1, -2, -1, -2]
di = [2, 1, -2, -1, 2, 1, -2, -1]

cnt = 0
for k in range(8):
    ni = i + di[k]
    nj = j + dj[k]
    if 0 <= ni < 8 and 0 <= nj < 8:
        cnt += 1
        
print(cnt)