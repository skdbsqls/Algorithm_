"2252 줄 세우기"

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1) 

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 핵심!! 진입차수 = 나에게 들어오는 화살표 = 나보다 앞에 있어야 하는 사람 수

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0: # 진입차수가 0이다? 맨 앞에 올 수 있다
        queue.append(i)

ans = []
while queue:
    cur = queue.popleft()
    ans.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*ans)