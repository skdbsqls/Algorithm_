import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    # 탐색하기
    deltas = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    my_queue = [[si, sj, 0]]
    maze[si][sj] = 0

    success = False
    distance = 0

    while my_queue:
        ti, tj, count = my_queue.pop(0)

        for delta in deltas:
            ni, nj = ti + delta[0], tj + delta[1]

            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] == 0:
                    my_queue.append([ni, nj, count + 1])
                    maze[ni][nj] = 1

                if maze[ni][nj] == 3:
                    success = True
                    distance = count
                    break

    if not success:
        distance = 0

    print(f'#{tc} {distance}')