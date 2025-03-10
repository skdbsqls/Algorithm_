import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # 터널의 세로, 터널의 가로, 맨홀 세로, 맨홀 가로, 소요된 시간
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]  # 지하 터널 지도
    deltas = [
        [-1, 0],  # 상
        [1, 0],  # 하
        [0, -1],  # 좌
        [0, 1],  # 우
    ]
    types = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],  # 1
        [1, 1, 0, 0],  # 2
        [0, 0, 1, 1],  # 3
        [1, 0, 0, 1],  # 4
        [0, 1, 0, 1],  # 5
        [0, 1, 1, 0],  # 6
        [1, 0, 1, 0],  # 7
    ]

    # BFS 탐색 준비
    queue = deque([[R, C, 1]])  # 시작점, 소요 시간
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1  # 시작점 방문 표시

    while queue:
        cx, cy, cnt = queue.popleft()  # 현재 위치, 현재 소요 시간
        cur_type = tunnel_map[cx][cy]  # 현재 위치의 구조물 종류

        # 시간을 다 소요 했으면,
        if cnt == L:
            break

        # 상하좌우 탐색
        for dir in range(4):  # dir : 상하좌우
            nx, ny = cx + deltas[dir][0], cy + deltas[dir][1]  # 다음 위치

            # 유효한 인덱스이면서
            if 0 <= nx < N and 0 <= ny < M:
                nex_type = tunnel_map[nx][ny]  # 다음 위치에 있는 구조물의 종류

                # 갈 수 있는 길인데, 아직 방문하지 않았다면
                if dir % 2 == 0:  # 현재 위치가 상좌일 때, 가야할 곳은 하우
                    if types[cur_type][dir] and types[nex_type][dir + 1] and not visited[nx][ny]:
                        queue.append([nx, ny, cnt + 1])
                        visited[nx][ny] = cnt + 1  # 방문 처리

                else:  # 현재 위치가 하우일 때, 가야할 곳은 상좌
                    if types[cur_type][dir] and types[nex_type][dir - 1] and not visited[nx][ny]:
                        queue.append([nx, ny, cnt + 1])
                        visited[nx][ny] = cnt + 1  # 방문 처리

    # 탈주범이 있을 수 있는 위치의 개수 찾기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                cnt += 1

    print(f'#{tc} {cnt}')