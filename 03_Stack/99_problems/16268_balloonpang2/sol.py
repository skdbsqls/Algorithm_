import sys

sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    deltas = [
        [0, 1],
        [1, 0],
        [-1, 0],
        [0, -1],
    ]
    result = 0  # 꽃가루의 최대 개수

    for i in range(N):
        for j in range(M):
            sum = arr[i][j]  # 꽃가루의 수

            for delta in deltas:
                # 유효한 인덱스라면
                if 0 <= i + delta[0] < N and 0 <= j + delta[1] < M:
                    ni = i + delta[0]
                    nj = j + delta[1]

                    # 꽃가루의 수 더하기
                    sum += arr[ni][nj]

            # 최댓값 갱신
            if result < sum:
                result = sum
                sum = 0  # 초기화

    print(f'#{tc} {result}')