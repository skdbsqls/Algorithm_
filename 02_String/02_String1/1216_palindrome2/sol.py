import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = input()
    arr = [list(input()) for _ in range(100)]

    # 가로 회문 검사
    def row_palindrome(arr, N):
        for i in range(100):
            for j in range(100 - N + 1):
                for k in range(N // 2):
                    if arr[i][j + k] != arr[i][j + N - 1 - k]:
                        break
                else:
                    return True

    # 세로 회문 검사
    def column_palindrome(arr, N):
        for j in range(100):
            for i in range(100 - N + 1):
                for k in range(N // 2):
                    if arr[i + k][j] != arr[i + N - 1 - k][j]:
                        break
                else:
                    return True

    result = 0  # 가장 긴 회문의 길이
    for N in range(1, 101):
        if row_palindrome(arr, N):
            result = N
        if column_palindrome(arr, N):
            result = N

    print(f'#{tc} {result}')