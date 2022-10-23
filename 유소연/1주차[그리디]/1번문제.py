from itertools import count


change = int(input('change : '))
coin = [500,100,50,10]
count = 0

for i in coin :
    count += change//i
    change = change%i

print(count)