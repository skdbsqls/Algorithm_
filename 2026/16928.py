"16928 뱀과 사다리 게임"

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 사다리 수, 뱀의 수
board = [i for i in range(101)] 

# 사다리 정보
for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

# 뱀 정보
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v


# BFS 준비
visited = [-1] * 101

queue = deque()
queue.append(1) # 시작점
visited[1] = 0 # 시작점 방문(시작할 때 주사위 횟수: 0)

# BFS 탐색
while queue:
    cur = queue.popleft()

    # 100(도착점)에 도달하면 종료
    if cur == 100:
        print(visited[cur])
        break
    
    # 주사위(1~6)
    for dice in range(1, 7):
        next = cur + dice # 이동할 칸

        # 100 넘으면 이동 X
        if next > 100:
            continue

        # 이동할 칸에 사다리 혹은 뱀이 있으면 적용
        next = board[next]

        # 방문하지 않았다면 이동
        if visited[next] == -1:
            visited[next] = visited[cur] + 1 # 주사위 굴린 횟수 = 이동 횟수
            queue.append(next)
