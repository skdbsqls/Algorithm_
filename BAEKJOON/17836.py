from collections import deque

N, M, T = map(int, input().split())  # (N * M)성, T시간
castle = [list(map(int, input().split())) for _ in range(N)]

deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque([[0, 0, 0, 0]])
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
result = float('inf')

while queue:
        i, j, t, find = queue.popleft()

        if i == N - 1 and j == M - 1:
            result = min(result, t)

        for di, dj in deltas:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj][find] == 0:
                if find == 1:
                    visited[ni][nj][find] = 1
                    queue.append([ni, nj, t + 1, find])
                else:
                    if castle[ni][nj] == 0:
                        visited[ni][nj][find] = 1
                        queue.append([ni, nj, t + 1, find])
                    elif castle[ni][nj] == 2:
                        visited[ni][nj][1] = 1
                        queue.append([ni, nj, t + 1, 1])

if result <= T:
    print(result)
else:
    print("Fail")