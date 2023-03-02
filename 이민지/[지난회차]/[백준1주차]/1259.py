while True:
    n = list(map(int,input()))
    if n==[0]:
        break
    isit = True
    for i in range(len(n)):
        if n[i]!=n[len(n)-1-i]:
            isit = False
    if isit==True:
        print("yes")
    else:
        print("no")
