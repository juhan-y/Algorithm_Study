x = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
y = ['1','2','3','4','5','6','7','8']
steps = [(-2,-1), (-1, -2), (1,-2), (2,-1), 
        (2,1), (1,2), (-1,2), (-2,1)]
count = 0
a, b = list(input())
a = x.index(a)
b = y.index(b)
for step in steps:
    c = a + step[0]
    d = b + step[1]
    if c>=0 and c<=7 and d>=0 and d<=7:
        count+=1
print(count)
