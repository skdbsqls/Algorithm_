from collections import deque

N, M, T = map(int, input().split()) # (N * M)성, T시간
castle = [list(map(int, input().split())) for _ in range(N)]

deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 델타
queue = deque([[0, 0, 0, 0]]) # [시작점, 시간, 그람 유무]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 방문여부
visited[0][0][0] = 1 # 시작점 방문 표시
result = float('inf') # 결과


while queue:
        i, j, t, find = queue.popleft() # 시작점(i, j), 소요 시간, 그람을 찾았는지 여부

        # 종료 지점에 도착했으면
        if i == N - 1 and j == M - 1:
            result = min(result, t) # 최소값 갱신

        for di, dj in deltas:
            ni, nj = i + di, j + dj

            # 범위 내에 있고, 방문하지 않았으면
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj][find] == 0:
                # 그람을 찾았으면(벽도 부수고 갈 수 있음)
                if find == 1:
                    visited[ni][nj][find] = 1
                    queue.append([ni, nj, t + 1, find])
                # 그람을 찾지 못 했으면
                else:
                    # 통로만 갈 수 있음
                    if castle[ni][nj] == 0:
                        visited[ni][nj][find] = 1
                        queue.append([ni, nj, t + 1, find])
                    # 그람을 찾았으면
                    elif castle[ni][nj] == 2:
                        # 그람을 찾았음을 표시
                        visited[ni][nj][1] = 1
                        queue.append([ni, nj, t + 1, 1])

if result <= T:
    print(result)
else:
    print("Fail")