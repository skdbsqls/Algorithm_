import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    string = input()
    N = len(string)

    result = 1
    for i in range(N // 2):
        if string[i] != string[N - 1 - i]:
            result = 0
            break

    print(f'#{tc} {result}')