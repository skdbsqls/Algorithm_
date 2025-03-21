import sys
sys.stdin = open('sample_input.txt')

INF = float('inf')

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())

    # 1. 인접리스트 만들기
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adj_list[start].append((end, weight))  # 유향 그래프

    # 2. 다익스트라 탐색 준비
    dists = [INF for _ in range(N + 1)]  # 현재 도달 가능한 정점들의 비용을 기록하기 위한 리스트
    visited = [False for _ in range(N + 1)]  # 방문 여부 표시
    dists[0] = 0  # 시작점 지정(시작점의 비용은 0)

    # 3. 다익스트라 탐색
    for _ in range(N + 1):  # 정점의 개수만큼 반복
        # 1) 아직 방문하지 않은 점들 중 가장 가까운 점에 방문
        # 1-1) 가장 가까운 점 찾기
        now = -1
        min_dist = INF
        for node in range(N + 1):
            # node를 방문한 적이 없으면서,
            # 내가 방문 가능한 점들 중 최단거리보다 node까지의 거리가 더 짧으면,
            if not visited[node] and dists[node] < min_dist:
                now = node
                min_dist = dists[node]

        # 1-2) 해당 점을 방문하기
        visited[now] = True

        # 2) 주변 정점들의 거리 갱신하기
        for node, weight in adj_list[now]:
            # 2-1) 해당 점을 방문한 적이 없다면,
            if not visited[node]:
                # 2-2) 거리 갱신하기
                # 원래 알고 있던 node로 가는 최저 비용과
                # now를 거쳐서 node로 가는 최저 비용을 비교
                dists[node] = min(dists[node], dists[now] + weight)

    print(f'#{tc} {dists[N]}')