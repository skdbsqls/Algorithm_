import sys
sys.stdin = open('sample_input.txt')

import heapq

def dijkstra(start_node):
    pqueue = [(0, start_node)]  # 누적거리, 시작노드
    dists = [INF] * (N + 1)  # 각 정점까지의 최단(누적)거리를 저장할 리스트
    dists[start_node] = 0  # 시작노드까지 최단거리는 0

    while pqueue:
        dist, node = heapq.heappop(pqueue)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            # 같거나 더 작은 가중치로 온 적이 있다면, continue
            if dists[next_node] <= new_dist:
                continue

            # next_node까지 도착하는데 드는 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pqueue, (new_dist, next_node))

    return dists


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N개의 정점, E개의 간선
    start_node = 0  # 0번 지점에서 시작
    INF = int(21e8)
    graph = [[] for _ in range(E)]  # 인접리스트

    # 인접리스트 만들기
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))  # 단방향 그래프

    result = dijkstra(start_node)
    ans = result[N]  # 끝점 N

    print(f'#{tc} {ans}')