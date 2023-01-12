def func(i):
    if i == 100:
        return
    print(i,'번 재귀 호출')
    func()

func(0)