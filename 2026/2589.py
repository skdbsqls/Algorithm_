"2589 보물섬"

import sys
input = sys.stdin.readline
from collections import deque

sero, garo = map(int, input().split())
treasure_map = [list(input().strip()) for _ in range(sero)]

# 육지인 곳만 뽑아내기(시작점)
starts = []
for i in range(sero):
    for j in range(garo):
        if treasure_map[i][j] == 'L':
            starts.append((i, j))

deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0

# 모든 시작점에서 최단 거리로 갈 수 있는 육지 중에 제일 먼 곳 찾기
for si, sj in starts:
    # bfs
    queue = deque()
    visited = [[0] * garo for _ in range(sero)]
    queue.append((si, sj, 0))
    visited[si][sj] = 1 
    max_v = 0 # 지금 시작점에서의 최댓값

    while queue:
        i, j, cnt = queue.popleft()

        # 지금 시작점에서의 최댓값 갱신
        if cnt > max_v:
            max_v = cnt

        for di, dj in deltas:
            ni, nj = i + di, j + dj

            if 0 <= ni < sero and 0 <= nj < garo:
                if treasure_map[ni][nj] == 'L' and not visited[ni][nj]:
                    queue.append((ni, nj, cnt + 1))
                    visited[ni][nj] = 1
    
    # 모든 시작점에서의 최댓값 갱신
    if max_v > ans:
        ans = max_v

print(ans)