# 1. 그래프
# - 그래프는 아이템들과 이들 사이의 연결 관계를 표현한다.
# - 그래프는 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료구조.
#   - V: 정점의 개수, E:간선의 개수
#   - V개의 정점을 가지는 그래프는 최대 V * (V - 1) / 2개이다.
# - 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N관계를 가지는 원소들을 표현하기에 용이하다.

# 2. 그래프의 유형
# - 무향 그래프: 방향성이 없다. (양방향이다)
# - 유향 그래프: 방향성이 존재한다. (팔로우/팔로잉)
# - 가중치 그래프
# - 사이클 없는 방향 그래프
# - 완전 그래프: 정점들에 대해 가능한 모든 간선들을 가진 그래프
# - 부분 그래프: 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

# 3. 그래프 용어
# - 인접(Adjacency): 두 개의 정점에 간선이 존재(연결됨)하면 서로 인접해 있다고 한다.
# - 경로: 간선들을 순서대로 나열한 것
# - 단순경로: 경로 중 한 정점을 최대한 한 번만 지나는 경로
# - 사이클: 시작한 정점에서 끝나는 경로

# 4. 그래프 표현
# - 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정한다.
# - 인접 행렬(Adjacent matrix): V * V 크기의 2차원 배열을 이용해서 간선 정보를 저장(배열의 (포인트)배열)
#   - V * V 정방 행렬
#   - 행 번호와 열 번호는 그래프의 정점에 대응
#   - 두 정점이 인접 되어 있으면 1, 그렇지 않으면 0으로 표현
#   - 단, 메모리 낭비가 심함
# - 인접 리스트(Adjacent List): 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
#   - 각 정점에 대한 인접 정점들을 순차적으로 표현
#   - 하나의 정점에 대한 인접 정점들을 각각 노드로 하는 연결리스트로 저장
#   - 두 정점의 인접 여부를 확인할 때, 검색 시간이 오래 걸린다.
# - 간선의 배열: 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

# ====================================================================================================
# 1. 그래프 순회(탐색)
# : 비선형구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미한다.

# 2. DFS(깊이우선탐색)
# : 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면,
#   가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 반복하여
#   결국 모든 정점을 방문하는 순회방법
# - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용
'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''


def dfs(node):
    # dfs의 경우 방문여부와, 확인할 후보가 정해져 있기 때문에 종료조건이 따로 필요 없음!
    # 보통 그래프 문제들에서, if문은 종료 시 해야할 것들 혹은 가지치기로 활용

    print(node, end=' ')

    # 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 만약, 이미 방문했다면 가지 말자.
        if visited[next_node]:
            continue

        # 만약, 방문하지 않았다면,
        visited[next_node] = 1  # 방문 표시 하고,
        dfs(next_node)  # 다음 노드로 진행


N, M = map(int, input().split())
# 그래프 저장하기(비어 있는 그래프를 생성하고, 정보를 입력 받아 넣기)
# graph = [[0] * (N + 1) for _ in range(N + 1)]  # 인접 행렬(N * N의 0 배열)
graph = [[] for _ in range(N + 1)]  # 인접 리스트(N * N의 [] 배열)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향이라면, 뒤집어서 저장도 해야만.

visited = [0] * (N + 1)  # 방문 여부 기록
visited[1] = 1  # 출발점 초기화
# dfs(1)  # 1 2 4 6 5 7 3


# 3. BFS(너비우선탐색)
# : 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에,
#   방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식이다.
# - 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로,
#   선입선출 형태의 자료구조인 큐를 활용한다.
'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

def bfs(start_node):
    # queue에 들어가는 노드들의 의미: 다음에 방문해야 할 노드들(대기열)
    queue = [start_node]  # 시작점을 넣은 상태로 출발

    while queue:
        # 1. 가장 앞에 있는 노드를 뽑는다.
        now = queue.pop(0)
        print(now, end=' ')

        # 인접한 노드들을 확인하면서,
        for next_node in graph[now]:
            # 방문 했으면 pass
            if visited[next_node]:
                continue

        # 2. 해당 노드에서 갈 수 있는 노드들을 queue에 넣는다.
        visited[next_node] = 1
        queue.append(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited[1] = 1
bfs(1)