import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N - M + 1):
            is_palindrome = True
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    is_palindrome = False
                    break

            if is_palindrome:
                for g in range(M):
                    result.append(arr[i][j + g])

    for j in range(N):
        for i in range(N - M + 1):
            is_palindrome = True
            for k in range(M // 2):
                if arr[i + k][j] != arr[i + M - 1 - k][j]:
                    is_palindrome = False
                    break

            if is_palindrome:
                for g in range(M):
                    result.append(arr[i + g][j])

    print(f'#{tc} {"".join(result)}')