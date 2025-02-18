import sys

sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    deltas = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]  # 8개 구역
    result = 0  # 예비 후보지의 수

    for i in range(N):
        for j in range(M):
            landing_spot = arr[i][j]  # 착륙 지점
            count = 0  # 사진을 찍을 수 있는 방향

            for delta in deltas:
                if 0 <= i + delta[0] < N and 0 <= j + delta[1] < M:
                    ni = i + delta[0]
                    nj = j + delta[1]

                    if landing_spot > arr[ni][nj]:  # 착륙 지점보다 낮으면
                        count += 1

            # 사진을 찍을 수 있는 방향이 4방향 이상이면, 예비 후보지
            if count >= 4:
                result += 1

    print(f'#{tc} {result}')