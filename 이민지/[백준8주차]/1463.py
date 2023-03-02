n = int(input())
d = {1:0,2:1}
def ans(n):
    if n in d:
        return d[n]
    d[n] = min(ans(n//3)+n%3,ans(n//2)+n%2)+1
    return d[n]
print(ans(n))