import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    word = input()
    N = len(word)

    result = 1
    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            result = 0

    print(f'#{tc} {result}')