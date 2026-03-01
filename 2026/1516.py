"1516 게임 개발"

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1) # 각 건물을 짓는데 걸리는 시간
indegree = [0] * (N + 1) # 해당 건물을 짓기 전에 필요한 건물의 개수

for i in range(1, N + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]

    # 선행 건물 정보 입력
    for pre in info[1:-1]:
        graph[pre].append(i)
        indegree[i] += 1

dp = [0] * (N + 1) # 각 건물을 짓는데 걸리는 총 시간

queue = deque()
for i in range(1, N + 1):
    # 선행 건물이 없으면 바로 큐에 넣기
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    cur = queue.popleft()
    
    for next in graph[cur]:
        indegree[next] -= 1
        # 기존값 vs 현재 건물을 짓는 시간 + 다음 건물을 짓는 시간 중 더 큰 값으로 갱신
        dp[next] = max(dp[next], dp[cur] + time[next])
        
        # 선행 건물이 없으면 큐에 넣기
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(dp[i])