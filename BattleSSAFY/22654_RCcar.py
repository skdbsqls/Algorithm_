import sys
sys.stdin = open('RCcarinput.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 필드의 크기
    field = [list(input()) for _ in range(N)]  # 필드
    Q = int(input())  # 조종 횟수
    results = []  # 결과

    # 시작점, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                si, sj = i, j  # 시작점

            if field[i][j] == 'Y':
                ei, ej = i, j  # 도착점

    # 델타
    deltas = [
        [-1, 0],  # 위
        [0, 1],   # 오른쪽
        [1, 0],   # 아래
        [0, -1],  # 왼쪽
    ]

    for _ in range(Q):
        result = '0'  # 커맨드 결과
        _, commands = input().split()  # 커맨드의 길이, 커맨드

        ti, tj = si, sj  # 시작점
        dir = 0  # RC카의 방향(처음에는 위쪽)

        for command in commands:
            if command == 'L':
                dir = (dir - 1) % 4

            if command == 'R':
                dir = (dir + 1) % 4

            if command == 'A':
                ni, nj = ti + deltas[dir][0], tj + deltas[dir][1]

                # 유효한 범위
                if 0 <= ni < N and 0 <= nj < N:
                    if field[ni][nj] == 'T':  # 나무는 이동 못 함
                        continue
                    ti, tj = ni, nj  # 그외에는 현위치 이동

        if ti == ei and tj == ej:
            result = '1'

        results.append(result)

    print(f'#{tc} {" ".join(results)}')


