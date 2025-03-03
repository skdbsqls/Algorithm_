import sys
sys.stdin = open('test_input.txt')

for _ in range(1, 11):
    tc = int(input())
    pattern = input()
    setence = input()

    count = 0
    for i in range(len(setence) - len(pattern) + 1):
        if setence[i:i + len(pattern)] == pattern:
            count += 1

    print(f'#{tc} {count}')

for _ in range(1, 11):
    tc = int(input())
    pattern = input()
    sentence = input()

    count = 0
    for i in range(len(sentence) - len(pattern) + 1):
        flag = True
        for j in range(len(pattern)):
            if sentence[i + j] != pattern[j]:
                flag = False
                break
        if flag:
            count += 1

    print(f'#{tc} {count}')