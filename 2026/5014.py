"5014 스타트링크"

from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

# bfs 준비
queue = deque()
queue.append(S)
visited = [-1] * (F + 1)
visited[S] = 0

# bfs 탐색
while queue:
    cur = queue.popleft()

    # 스타트링크에 도착하면 종료
    if cur == G:
        print(visited[G])
        sys.exit(0)
    
    # 위, 아래
    for next in (cur + U, cur - D):
        # 갈 수 있는 범위 안에 있으면서 방문 안 했으면
        if 0 < next <= F and visited[next] == -1:
            visited[next] = visited[cur] + 1
            queue.append(next)

# 도착 못 한 경우
print("use the stairs")