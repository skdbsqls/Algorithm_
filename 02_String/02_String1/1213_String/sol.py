
for _ in range(10):
    tc = input()
    target = input()
    sentence = input()

    sentence_lst = sentence.split(target)
    result = len(sentence_lst) - 1

    print(f'#{tc} {result}')