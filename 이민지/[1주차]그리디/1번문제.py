n = int(input())
sum = 0
sum += n/500
n = n%500
sum += n/100
n = n%100
sum += n/50
n = n%50
sum += n/10
n = n%10
print(sum)
