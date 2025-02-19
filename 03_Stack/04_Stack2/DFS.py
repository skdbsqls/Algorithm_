# DFS(깊이 우선 탐색)
# 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가,
# 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간석이 있는 정점으로 되돌아와서,
# 다른 방향의 정점으로 탐색을 계속 반복하여
# 결국 모든 정점을 방문하는 순회 방법이다.
# -> 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 탐색을 반복해야 하므로,
# -> 후입선출 구조의 스택을 사용한다.

node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

def dfs(s, V):  # s: start, V: 정점의 개수
    visited = [0]*(V+1)
    stack = []

    i = s  # 현재 방문한 정점 i
    visited[i] = 1  # 방문 표시 하기

    # 문제에 따라 달라지는 부분..
    print(node[i], end=' ')

    while i != 0:  # i가 0이라는 것은 더이상 갈 곳이 없다는 뜻

        # 1부터 V번까지 정점을 확인하면서
        for w in range(1, V+1):

            # 현재 방문한 정점과 연결되어 있고, 방문한 적이 없다면,
            if adj[i][w] == 1 and visited[w] == 0:
                stack.append(i)  # 방문 경로 저장
                i = w            # 새 방문지 이동
                visited[w] = 1   # 중복 방문 방지
                print(node[i], end=' ')
                break
        # 다음 정점이 없으면
        else:
            # 스택이 비어있지 않으면,
            if stack:
                i = stack.pop()  # 가장 마지막에 만났던 정점으로 되돌아가면 된다.
            # 스택이 비어 있으면,
            else:
                i = 0  # 돌아갈 곳이 없다는 뜻
                # break
    return

#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
dfs(1, 7)

# *[문제에서 DFS 활용하기]

v = 7  # 정점의 개수
e = 8  # 간선의 개수
# 간선의 정보
edges = [
    [1, 2],
    [1, 3],
    [2, 4],
    [2, 5],
    [4, 6],
    [5, 6],
    [6, 7],
    [3, 7],
]

# 간선 정보를 인접 행렬 형태로 만들기
adj_mat = [
    # [0] * (v + 1) : (정점의 개수 + 1) 개의 0을 가진 리스트
    # for _ in range(v + 1) : 반복해서 adj_mat를 채운다
    [0] * (v + 1) for _ in range(v + 1)
]

# 각 간선 정보를 확인하며 adj_mat 완성하기
for edge in edges:
    # edge[0]과 edge[1]은 서로 양뱡향으로 연결되어 있다.
    adj_mat[edge[0]][edge[1]] = 1
    adj_mat[edge[1]][edge[0]] = 1

# adj_mat 출력
for row in adj_mat:
    print(row)

# [DFS 준비하기]

# 재방문 방지를 위해 visited를 만든다.
visited = [False for _ in range(v + 1)]

# 1번에서 출발하기 때문에,
visited[1] = True

# 진행 경로를 저장할 리스트를 만든다.
route = []

# 방문할 대상을 저장할 stack을 만든다.
stack = [1]

# stack이 비어 있지 않는 동안 반복한다.
while stack:
    # 이번에 방문할 곳을 stack에서 가져온다.
    now = stack.pop()
    # 진행 경로를 리스트에 저장한다. <- 문제에 따라 달라지는 부분
    route.append(now)
    # 내가 다음에 방문할 수 있는 정점들을 크기의 역순으로 stack에 넣어준다.
    for next in range(v, 0, -1):  # (0, v)라면 더 큰 수부터 방문...
        # 연결이 되어 있고, 방문한 적이 없으면, 방문 예정으로 stack에 넣어준다.
        if adj_mat[now][next] == 1 and not visited[next]:
            stack.append(next)
            # 방문 예정임으로,
            visited[next] = True

print(route)  # [1, 2, 4, 6, 7, 5, 3]

# [연습문제] 미로 (델타 + DFS)
N = int(input())

maze = []
start = end = None

# n개의 줄 입력, 그 중 몇 개는 시작 또는 끝
for i in range(N):
    row = list(map(int, input()))

    # 해당 줄에 시작 또는 끝이 있는지 확인
    for j in range(N):
        # 시작점
        if row[j] == 2:
            start = [i, j]
            row[j] = 1  # 방문 했음으로 처리
        # 끝점
        if row[j] == 3:
            end = [i, j]
            row[j] = 0  # 방문 가능함으로 처리

    # 줄을 검사 했으면 maze에 추가
    maze.append(row)

print(maze)
'''
[
[1, 3, 1, 0, 1], 
[1, 0, 1, 0, 1], 
[1, 0, 1, 0, 1], 
[1, 0, 1, 0, 1], 
[1, 0, 0, 1, 1]
]
'''

# 델타 준비하기
deltas = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]
# maze 자체를 visited로 쓸 것이기 때문에 visited를 따로 만들 필요가 없다.
# 지나온 길은 다시 갈 수 없도록 방문 했음(1) 처리 해주면 되기 때문이다.

# stack을 만들고, 첫방문 예정지를 start로 한다.
stack = [start]
# end에 도달하면 성공한 것이다.
success = False

# 갈 곳이 남아 있고, 아직 도달하지 못 했다면 반복
while stack and not success:
    # 이번에 방문할 곳을 stack에서 가져온다.
    now = stack.pop()

    # 델타 탐색을 통해 주변을 살핀다.
    for delta in deltas:
        next_i = now[0] + delta[0]
        next_j = now[1] + delta[1]

        # 미로 내부에 있으며, 벽이 아닌 경우
        if not (0 <= next_i < N and 0 <= next_j < N and maze[next_i][next_j] == 0):
            continue

        # 방문 처리, 이미 방문한 곳(지나온 곳)은 벽으로 만든다.
        maze[next_i][next_j] = 1
        # 그 다음 방문 예정으로 추가한다.
        stack.append([next_i, next_j])

        # 만약 해당 점이 목적이 였다면,
        if next_i == end[0] and next_j == end[1]:
            success = True  # 성공이다!
            break

print(maze)
print(success)