n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)
words = list(set(words)) # 중복제거
words_sorted = sorted(words, key=lambda x:(len(x), x)) # 정렬
for i in words_sorted:
    print(i)
