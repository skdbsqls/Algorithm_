import sys

sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합 중 최댓값 찾기
    row_max = 0
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if row_max < row_sum:
            row_max = row_sum

    # 각 열의 합 중 최댓값 찾기
    col_max = 0
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if col_max < col_sum:
            col_max = col_sum

    # 각 대각선의 합 중 최댓값 찾기
    dia_max = 0
    sum1 = sum2 = 0
    for i in range(100):
        sum1 += arr[i][i]
        sum2 += arr[i][99 - i]

        if sum1 > sum2:
            dia_max = sum1
        else:
            dia_max = sum2

    # 세 개의 최댓값 중에서 최종 최댓값 찾기
    result = max([row_max, col_max, dia_max])

    print(f'#{test_case} {result}')