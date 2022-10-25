n, m, k = map(int, input().split())
my_list = list(map(int, input().split()))
my_list.sort()
i = m%k
j = m-i
print(my_list[-1]*j + my_list[-2]*i)