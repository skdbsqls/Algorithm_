from collections import deque

N, M, K = map(int, input().split()) # 세로, 가로, 개수
matrix = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split()) # 좌표
    matrix[r-1][c-1] = 1 # 음식물 있는 곳 표시

# 델타 
deltas = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]
visited = [[0] * M for _ in range(N)] # 방문 여부
result = 0 # 결과

for i in range(N):
    for j in range(M):
        # 음식물이 있는 곳(시작점이 될 수 있는 곳)이면서 방문하지 않은 곳이라면
        if matrix[i][j] == 1 and visited[i][j] == 0:
            queue = deque([[i, j]]) # BFS 탐색할거야
            visited[i][j] = 1 # 시작점 방문 표시
            cnt = 1 # 음식물 크기

            while queue:
                x, y = queue.popleft()
                # 최댓값 갱신
                if cnt > result:
                    result = cnt

                # 델타 탐색하면서(상하좌우 인접하면 음식물끼리 붙음)
                for delta in deltas:
                    nx = x + delta[0]
                    ny = y + delta[1]

                    # 유효한 범위 내에 있고
                    if 0 <= nx < N and 0 <= ny < M:
                        # 방문해야 하는 곳(음식물이 있는 곳 == 1)이면서 방문하지 않은 곳이라면
                        if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                            queue.append([nx, ny]) # 큐에 삽입
                            visited[nx][ny] = 1 # 방문 표시
                            cnt += 1 # 개수 갱신

print(result)

# BFS로 풀었지만 DFS(stack)으로 풀어도 똑같은 결과가 나옴