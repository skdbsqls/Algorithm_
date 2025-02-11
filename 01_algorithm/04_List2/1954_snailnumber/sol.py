import sys

sys.stdin = open('input.txt')

T = int(input())

# 풀이 1)
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


# 풀이 2)
N = 4
# 달팽이가 될 2차원 배열 선언
result = [[0] * N for _ in range(N)]

# 우하좌상 순서대로 델타 선언
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 현재 방향
dir_idx = 0

# 현재 위치
now_i = 0
now_j = 0

# 달팽이 숫자 만들기
for next_num in range(1, N * N + 1):
    # 현재 위치에 숫자 넣기
    result[now_i][now_j] = next_num

    # 현재 진행방향으로 더 진행할 수 있는지 판단
    # 인덱스가 유효한지, 다음 위치에 0이 있는지를 기준으로
    if not (0 <= now_i + di[dir_idx] < N and 0 <= now_j + dj[dir_idx] < N and result[now_i + di[dir_idx]][now_j + dj[dir_idx]] == 0):
        # 만약 그렇지 않으면, 방향 전환
        dir_idx = (dir_idx + 1) % 4

    # 다음 위치 지정
    now_i += di[dir_idx]
    now_j += dj[dir_idx]

for row in result:
    print(f'{" ".join(map(str, row))}')
