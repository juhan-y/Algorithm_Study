import sys
n, m = map(int, sys.stdin.readline().split())
pokemon_name = {} # 이름이 키, 번호가 값
pokemon_num = {} # 번호가 키, 이름이 값
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    pokemon_name[name] = i
    pokemon_num[i] = name

for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True:
        print(pokemon_num[int(item)])
    else:
        print(pokemon_name[item])

