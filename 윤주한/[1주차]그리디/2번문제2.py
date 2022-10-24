n, m, k = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort(reverse=True)

result = (m//(k+1)) * (ls[0]*k+ls[1])
result += (m%(k+1)) * ls[0]

print(result)