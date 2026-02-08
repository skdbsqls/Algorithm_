"13460 구슬 탈출 2"

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 세로 가로
board = [list(input().strip()) for _ in range(N)] # 보드

# 빨간 구슬, 파란 구슬의 시작점 찾기
rx = ry = bx = by = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

# BFS 준비
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# visited[rx][ry][bx][by] = (R, B 위치 조합 상태 방문 여부)
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rx][ry][bx][by] = 1

queue = deque()
queue.append((rx, ry, bx, by, 0))

ans = -1
success = False # 성공 여부

# BFS 탐색
while queue and not success:
    crx, cry, cbx, cby, cnt = queue.popleft()

    # 10번 넘어가면 실패
    if cnt >= 10:
        break

    # 상하좌우
    for dx, dy in dirs:

        # 빨간 구슬 이동
        nrx, nry = crx, cry
        r_cnt = 0

        # 현재 칸이 구멍이 아니고, 다음 칸이 벽이 아닐 때까지 계속
        while board[nrx][nry] != 'O' and board[nrx + dx][nry + dy] != "#":
            nrx += dx
            nry += dy
            r_cnt += 1

        
        # 파란 구슬 이동
        nbx, nby = cbx, cby
        b_cnt = 0
        while board[nbx][nby] != 'O' and board[nbx + dx][nby + dy] != '#':
            nbx += dx
            nby += dy
            b_cnt += 1
        
        # 다 이동 했을 때, 파란 구슬이 구멍에 빠지면 실패 -> 다음 방향 시도
        if board[nbx][nby] == 'O':
            continue

        # 빨간 구슬이 빠지면 성공   
        if board[nrx][nry] == 'O':
            ans = cnt + 1
            success = True
            break

        # 둘 다 구멍에 안 빠졌는데, 만약 빨간 구슬과 파란 구슬의 위치가 같으면 위치 조정이 필요
        if nrx == nbx and nry == nby:
            # 더 뒤에서 이동한 구슬(더 많이 움직인 구슬)을 한 칸 뒤로
            if r_cnt > b_cnt:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy
        
        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = 1
            queue.append((nrx, nry, nbx, nby, cnt + 1))

print(ans)