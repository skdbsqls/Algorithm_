import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    snail[0][0] = 1  # snail[0][0]은 무조건 1

    datels = [
        [0, 1],   # 우
        [1, 0],   # 하
        [0, -1],  # 좌
        [-1, 0],  # 상
    ]
    dir = 0  # 방향

    num = 2  # 2부터 시작
    i = j = 0  # 위치
    while num <= N * N:
        ni = i + datels[dir][0]
        nj = j + datels[dir][1]

        # 유효한 인덱스이고, 비어있다면,
        if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
            snail[ni][nj] = num  # 알맞은 위치에 숫자 삽입
            i, j = ni, nj  # 위치 갱신
            num += 1  # 숫자 + 1

        else:
            dir = (dir + 1) % 4  # 방향 전환

    print(f'#{tc}')
    for s in snail:
        print(f'{" ".join(map(str, s))}')