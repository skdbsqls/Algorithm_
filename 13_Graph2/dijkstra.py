# [최단 경로]

# 1. 최단 경로 정의
# : 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로

# 2. 하나의 시작 정점에서 끝 정점까지의 최단경로
# - 다익스트라(dijkstra) 알고리즘
#   : 음의 가중치를 허용하지 않음(양수와 음수가 섞여 있는 문제에는 적용X)
# - 벨만-포드(Bellman-Ford) 알고리즘
#   : 음의 가중치 허용

# 3. 모든 정점들에 대한 최단 경로
# - 폴로이드-워샬(Floyd-Warshall) 알고리즘

# =========================================================================================
# [Dijkstra 알고리즘]
# - 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.
# - 시작 정점(s)에서 끝 정점(t)까지 최단 경로에 정점 x가 존재한다.
# - 이때, 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성된다.
# - 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''


def dijkstra(start_node):
    pq = [(0, start_node)]  # (누적거리, 노드번호)
    dists = [INF] * V  # 각 정점까지의 최단(누적)거리를 저장할 리스트
    dists[start_node] = 0  # 시작노드 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]  # 다음 노드로 가기 위한 가중치
            next_node = next_info[1]  # 다음 노드 번호

            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            # 같거나 더 작은 가중치로 온 적이 있다면, continue
            if dists[next_node] <= new_dist:
                continue

            # next_node까지 도착하는데 드는 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists


import heapq
INF = int(21e8)  # 21억(무한대를 의미한다고 가정)

V, E = map(int, input().split())
start_node = 0  # 문제에 따라 다름
graph = [[] for _ in range(V)]  # 인접 리스트로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # 단방향 그래프

# result_dists: 0에서 출발해서, 다른 노드들까지의 최단 거리를 모두 구함
result_dists = dijkstra(0)
print(result_dists)