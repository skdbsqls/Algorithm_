import sys
sys.stdin = open('sample_input.txt')

from collections import deque

deltas = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
]  # 델타

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())  # 구슬을 쏠 수 있는 횟수, 벽들의 가로, 세로
    bricks = [list(map(int, input().split())) for _ in range(H)]  # 벽돌

    remain_bricks = 0  # 깨야할 벽돌의 개수
    for i in range(H):
        for j in range(W):
            if bricks[i][j]:
                remain_bricks += 1




# def shoot(cnt, remain_bricks, now_bricks):
#     global min_bricks
#
#     # 구슬을 다 떨어뜨렸다면...
#     if cnt == N or remain_bricks == 0:
#         min_bricks = min(min_bricks, remain_bricks)
#         return
#
#     # w번 돌면서 구슬을 떨어뜨려보자.
#     for col in range(W):
#         copy_bricks = [row[:] for row in now_bricks]  # 현재 상태 복사하기
#         row = -1  # 가장 위에 있는 벽돌의 위치
#
#         for j in range(H):
#
#             # 가장 위에 있는 벽돌의 위치 찾기
#             if copy_bricks[j][col]:
#                 row = j
#                 break
#
#         if row == -1:  # 벽돌이 없는 열이면 다음 열로 넘어가기
#             continue
#
#         # BFS 탐색 준비
#         queue = deque([(row, col, copy_bricks[row][col])])  # 현재 위치, 벽돌의 숫자
#         copy_bricks[row][col] = 0  # 시작점 방문 처리
#         now_remain_bricks = remain_bricks - 1  # 깨진 벽돌의 개수(시작점 1개)
#
#         # BFS 탐색하기
#         while queue:
#             cx, cy, num = queue.popleft()  # 현재 위치, 벽돌의 숫자
#
#             for k in range(1, num + 1):  # 벽돌의 숫자만큼 멀리까지 탐색
#                 for delta in deltas:
#                     nx, ny = cx + (delta[0] * k), cy + (delta[1] * k)
#
#                     if 0 <= nx < H and 0 <= ny < W:
#                         if copy_bricks[nx][ny]:
#                             queue.append([nx, ny, copy_bricks[nx][ny]])
#                             copy_bricks[nx][ny] = 0
#                             now_remain_bricks -= 1  # 벽돌 세기
#
#         # 빈칸 메꾸기(벽돌이 깨진 후 다음 상태 만들기)
#         for c in range(W):
#             idx = H - 1
#             for r in range(H - 1, -1, -1):  # 밑에서부터
#                 if copy_bricks[r][c]:
#                     copy_bricks[r][c], copy_bricks[idx][c] = copy_bricks[idx][c], copy_bricks[r][c]
#                     idx -= 1
#
#         shoot(cnt + 1, now_remain_bricks, copy_bricks)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())  # 구슬을 쏠 수 있는 횟수, 벽들의 가로, 세로
#     bricks = [list(map(int, input().split())) for _ in range(H)]  # 벽돌
#
#     remain_bricks = 0  # 깨야할 벽돌의 개수
#     for i in range(H):
#         for j in range(W):
#             if bricks[i][j]:
#                 remain_bricks += 1
#
#     min_bricks = 1e9
#     shoot(0, remain_bricks, bricks)
#
#     print(f'#{tc} {min_bricks}')