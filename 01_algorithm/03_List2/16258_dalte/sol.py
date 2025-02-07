import sys

sys.stdin = open('in.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 총합
    daltes = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]

    for i in range(N):
        for j in range(N):
            for di, dj in daltes:
                ni, nj = i + di, j + dj

                # 유효한 인덱스 확인
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(arr[ni][nj] - arr[i][j])

    print(f'#{test_case} {result}')