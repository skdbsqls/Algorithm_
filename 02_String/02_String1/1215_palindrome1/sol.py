import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    result = 0
    for i in range(8):
        for j in range(8 - N + 1):
            is_palindrome = True
            for k in range(N // 2):
                if arr[i][j + k] != arr[i][j + N - 1 - k]:
                    is_palindrome = False
                    break

            if is_palindrome:
                result += 1


    for j in range(8):
        for i in range(8 - N + 1):
            is_palindrome = True
            for k in range(N // 2):
                if arr[i + k][j] != arr[i + N - 1 - k][j]:
                    is_palindrome = False
                    break

            if is_palindrome:
                result += 1

    print(f'#{tc} {result}')