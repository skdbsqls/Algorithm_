import sys

sys.stdin = open('input.txt')

for i in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지의 x, y 좌표
    x = ladder[99].index(2)
    y = 99

    # 방향
    daltes = [
        [-1, 0],  # 좌
        [1, 0],   # 우
        [0, -1],  # 상
    ]
    dir = 0

    # 출발지에 도착할 떄까지 반복
    while y > 0:
        # 이동하기
        nx = x + daltes[dir][0]
        ny = y + daltes[dir][1]

        # 유효한 인덱스이고, 1이라면(사다리가 있다면)
        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[ny][nx]:
            # 지나간 자리는 0으로
            ladder[ny][nx] = 0

            # x, y 위치 갱신
            x = nx
            y = ny

            # 방향도 초기화
            dir = 0

        # 방향 바꾸기
        else:
            dir = (dir + 1) % 3

    print(f'#{T} {x}')