# [최소 비용 신장 트리(MST)]
# 1. 그래프에서 최소 비용 문제
# - 모든 정점을 연갈하는 간선들의 가중치의 합의 최소가 되는 트리(MST)
# - 두 정점 사이의 최소 비용의 경로 찾기(최단거리)

# 2. 신장 트리
# : n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

# 3. 최소 신장 트리(Minimum Spanning Tree)
# : 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합의 최소인 신장 트리


# ============================================================================================
# [Prim 알고리즘]
# 하나의 정점에서 연결된 간선들 중 하나씩 선택하면서 MST를 만들어 가는 방식
# 1) 임의 정점을 하나 선택해서 시작
# 2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
# 3) 모든 정점이 선택될 때까지 1-2과정을 반복

# 서로소인 2개의 집합 정보를 유지
# 트리 정점들 - MST를 만들기 위해 선택된 정점들
# 비트리 정점들 - 선택되지 않은 정점들
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# [prim 알고리즘]
# - 특정 정점을 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 고르기
# -> 그냥 큐가 아닌, 우선순위 큐를 활용하자!
import heapq


def prim(start_node):
    pqueue = [(0, start_node)]  # 시작점은 가중치가 0
    MST = [0] * V  # visited와 동일
    min_weight = 0  # 최소 비용

    while pqueue:
        weight, node = heapq.heappop(pqueue)  # 가중치와 노드

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue

        MST[node] = 1  # 방문처리
        min_weight += weight  # 누적합 추가

        for next_node in range(V):
            # 갈 수 없으면 pass
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 pass
            if MST[next_node]:
                continue

            heapq.heappush(pqueue, (graph[node][next_node], next_node))

    return min_weight


V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]  # 인접행렬

for _ in range(E):
    start, end, weight = map(int, input().split())  # 시작점, 끝점, 가중치
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)
print(f'최소 비용 = {result}')  # 최소 비용 = 175


# ============================================================================================
# [Kruskal 알고리즘]
# - 간선을 하나씩 선택해서 MST를 찾는 알고리즘
# - 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
# - 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킨
#   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
#   - 같은 집합끼리 연결하면 사이클 발생(union-find)
# - n-1개의 간선이 선택될 때까지 반복,,

# [Kruskal]
# - 모든 간선들을 보면서
#   - 가중치가 작은 간선부터 고르자(정렬)
#   - 이때, 사이클이 발생하면 pass


def find_set(x):
    if x == parents[x]:
        return x

    # return find_set(parents[x])  => 기본
    parents[x] = find_set(parents[x])  # => 경로 압축
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 사이클 방지
    if ref_x == ref_y:
        return

    # 일정한 규칙으로 연결
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))  # 간선에 대한 정보들 저장

edges.sort(key=lambda x: x[2])  # 가중치를 기준으로 오름차순 정렬
# for edge in edges:
#     print(edge)
parents = [i for i in range(V)]

# 작은 것부터 고르면서 나아가자
# 언제까지? N-1개를 선택할 때까지
cnt = 0  # 현재까지 선택한 간선의 수
result = 0  # MST 가중치의 합

for u, v, w in edges:
    # start와 end가 연결이 되어 있지 않으면 선택(=다른 집합이라면 선택)
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:  # MST 구성이 끝남
            break

print(result)

# ============================================================================================
# [Prim과 Kruskal 비교]

# prim의 시간복잡도: O((V + E)logV)
#   - 보통 정점보다 간선이 더 많음
#   -> O(ElogV)
#   - 간선을 모두 고려하면서 우선순위큐에 넣어야 함
#   -> 간선의 수가 적을수록 유리

# Kruskal의 시간복잡도: O(ElogE)
#   - 간선 위주로 정렬하는 시간만 필요
#   -> 간선의 수가 많을 때만 유리