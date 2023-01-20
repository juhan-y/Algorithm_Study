import sys

cnt = int(sys.stdin.readline().rstrip())

words = []
max_len = 0
for _ in range(cnt):
    input_word = sys.stdin.readline().rstrip()
    words.append(input_word)
    max_len = max(max_len,len(input_word))

words_for_len = [[] for _ in range(max_len+1)]

for word in words:
    idx = len(word)
    if word not in words_for_len[idx]:
        words_for_len[idx].append(word)
        words_for_len[idx].sort()

for words in words_for_len:
    for word in words:
        print(word)

