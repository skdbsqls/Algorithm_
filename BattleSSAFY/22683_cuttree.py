import sys
sys.stdin = open('cuttreeinput.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                si, sj = i, j
            if field[i][j] == 'Y':
                ei, ej = i, j

    # 좌표(i, j), 방향, 나무를 벤 횟수
    visited = [[[[0] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]

    # 탐색 준비
    deltas = [
        [-1, 0],  # 위
        [0, 1],   # 오른쪽
        [1, 0],   # 아래
        [0, -1],  # 왼쪽
    ]

    queue = [[si, sj, 0, 0, 0]]  # 시작점, 조작 횟수, 방향, 나무를 벤 횟수, 조작 횟수
    visited[si][sj][0][0] = 1  # 방문처리
    ans = -1  # 결과

    while queue:
        ti, tj, dir, cut, cmd = queue.pop(0)  # 현재 위치, 현재 조작 횟수

        # 도착점에 도달한 경우
        if (ti, tj) == (ei, ej):
            ans = cmd
            break

        # R(우회전)
        nd = (dir + 1) % 4
        if not visited[ti][tj][nd][cut]:
            visited[ti][tj][nd][cut] = 1
            queue.append([ti, tj, nd, cut, cmd + 1])

        # L(좌회전)
        nd = (dir - 1) % 4
        if not visited[ti][tj][nd][cut]:
            visited[ti][tj][nd][cut] = 1
            queue.append([ti, tj, nd, cut, cmd + 1])

        # A(전진)
        ni, nj = ti + deltas[dir][0], tj + deltas[dir][1]
        if 0 <= ni < N and 0 <= nj < N:
            # 땅이거나 도착지인 경우,
            if field[ni][nj] == 'G' or field[ni][nj] == 'Y':
                if not visited[ni][nj][dir][cut]:
                    visited[ni][nj][dir][cut] = 1
                    queue.append([ni, nj, dir, cut, cmd + 1])

            # 나무이면서 나무를 벨 수 있는 횟수가 남은 경우,
            elif field[ni][nj] == 'T' and cut < K:
                if not visited[ni][nj][dir][cut]:
                    visited[ni][nj][dir][cut] = 1
                    queue.append([ni, nj, dir, cut + 1, cmd + 1])

    print(f'#{tc} {ans}')


