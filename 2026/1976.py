"1976 여행 가자"

import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # N개의 도시
M = int(input()) # M개의 여행 계획 도시

graph = [[] for _ in range(N)] # 인접 리스트
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            graph[i].append(j)
'''
graph = [
    [1],      
    [0, 2],   
    [1]       
]
'''

citys = list(map(int, input().split())) # 여행 계획

# bfs
visit = [0] * N
queue = deque()
queue.append(citys[0] - 1) # 시작점
visit[citys[0] - 1] = 1 # 방문표시

while queue:
    cur = queue.popleft()
    for next in graph[cur]:
        if visit[next] == 0:
            visit[next] = 1
            queue.append(next)

# 결과
for city in citys:
    if visit[city - 1] == 0:
        print("NO")
        break
else:
    print("YES")