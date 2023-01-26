n = int(input())

texts = []

for _ in range(n):
  texts.append(input())
texts = list(set(texts))
texts.sort(key = lambda x: (len(x), x))



for text in texts:
  print(text)