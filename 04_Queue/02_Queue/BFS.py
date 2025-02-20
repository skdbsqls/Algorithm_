# BFS(Breadth First Search, 너비우선탐색)
# : 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에 방문했던 정점을 시작점을 하여 다시 인접한 정점들을 차례로 방문하는 방식
# * 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용한다.
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())  # V : 정점, E : 간선
arr = list(map(int, input().split()))

# 인접 리스트
adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# BFS
def bfs(S, V):  # S : 시작 정점, V : 마지막 정점
    visited = [0] * (V + 1)  # visited 생성
    my_queue = []  # queue 생성

    my_queue.append(S)  # 시작점 enqueue
    visited[S] = 1  # 시작점 enqueue 표시

    # queue가 비워질 때까지 반복(front != rear)
    while my_queue:
        t = my_queue.pop(0)  # dequeue해서 t에 저장
        print(t)  # t 정점에 대한 처리(문제에 따라 다르게 처리)

        # t에 인접한 정점 w 중에서, enqueue되지 않은 정점이 있으면,
        for w in adj_list[t]:
            if visited[w] == 0:
                my_queue.append(w)  # enqueue
                visited[w] = visited[t] + 1  # enqueue 표시

    print(visited)  # [0, 3, 2, 4, 3, 1, 2, 3]

bfs(1, V)
'''
1
2
3
4
5
7
6
'''

# [연습문제] 미로의 거리
def bfs(i, j, N):  # i, j : 시작 위치, N : 크기
    visited = [[0] * N for _ in range(N)]  # visited 생성
    queue = []  # queue 생성

    queue.append([i, j])  # 시작점 enqueue
    visited[i][j] = 1  # 시작점 enqueue 표시

    # 큐가 비워질 때까지 반복하기
    while queue:
        ti, tj = queue.pop(0)  # dequeue

        if maze[ti][tj] == '3':
            # return 1  # 끝점(3)에 도착하면 1 아니면 0 return인 경우
            return visited[ti][tj] - 2  # 시작점에서 끝점까지 지나야 하는 최소한의 칸 수를 구해야 하는 경우(시작점, 끝점 빼줘야 함)

        # t에 인접한 w 중, enqueue되지 않은 곳
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj

            # 미로를 벗어 나지 않으면서, 벽이 아니면서, 방문하지 않은 곳이라면,
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                queue.append([wi, wj])  # enqueue
                visited[wi][wj] = visited[ti][tj] + 1  # enqueue 표시

    return 0  # 끝점(3)에 도착하면 1 아니면 0 return인 경우


def find_start(N):  # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기
    maze = [input() for _ in range(N)]

    sti, stj = find_start(N)
    result = bfs(sti, stj, V)

    print(f'#{tc} {result}')





















