import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs(N):
    queue = deque([N])  # N에서 시작

    while True:
        now = queue.popleft()

        if now == M:  # M이 되면 끝!
            break

        for i in range(4):
            if i == 0:
                next = now + 1
            if i == 1:
                next = now - 1
            if i == 2:
                next = now * 2
            if i == 3:
                next = now - 10

            # 백만 이하의 자연수
            if 0 < next < 1000001 and not visited[next]:
                queue.append(next)
                visited[next] = visited[now] + 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    visited[N] = 0
    bfs(N)

    print(f'#{tc} {visited[M]}')