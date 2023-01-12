while True:
    ls = list(map(int, input().split()))
    if ls[0] == 0 and ls[1] == 0 and ls[2] == 0:
        break
    ls.sort()
    if ls[2]**2 == ls[0]**2 + ls[1]**2:
        print("right")
    else:
        print("wrong")