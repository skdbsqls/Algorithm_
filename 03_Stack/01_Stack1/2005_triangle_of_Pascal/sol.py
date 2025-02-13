import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    result = [[0] * N for _ in range(N)]  # N * N 2차원 배열 만들기
    result[0][0] = 1  # 첫 번째 줄은 항상 1

    for i in range(1, N):
        for j in range(i + 1):

            # 두 번째 줄 이상도 첫 번째 수는 항상 0
            if j == 0:
                result[i][j] = 1

            # 위치에 맞게 왼쪽과 오른쪽 위의 숫자의 합을 넣어줌
            else:
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    # 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            # 0이 아닐 경우에만 출력
            if result[i][j]:
                print(result[i][j], end=' ')
        print()