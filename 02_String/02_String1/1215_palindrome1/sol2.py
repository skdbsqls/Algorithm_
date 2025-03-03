import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    matrix = [input() for _ in range(8)]
    count = 0

    for i in range(8):
        for j in range(8 - N + 1):
            row_flag = True
            col_flag = True

            for k in range(N // 2):
                if matrix[i][j + k] != matrix[i][j + N - 1 - k]:
                    row_flag = False

                if matrix[j + k][i] != matrix[j + N - 1 - k][i]:
                    col_flag = False

            count += row_flag + col_flag

    print(f'#{tc} {count}')