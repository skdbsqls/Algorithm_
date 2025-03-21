import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트 만들기
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append((n2, w))
        adj_list[n2].append((n1, w))

    # 준비
    dists = [11 for _ in range(V + 1)]  # 각 정점까지 도달할 수 있는 최소 거리 모음
    visited = [False for _ in range(V + 1)]  # 방문여부
    dists[0] = 0  # 시작점은 0, 시작점까지 거리는 0

    # prim
    for _ in range(V + 1):
        now = -1
        min_dist = 11

        for n in range(V + 1):
            if not visited[n] and dists[n] < min_dist:
                min_dist = dists[n]
                now = n

        visited[now] = True

        for n, w in adj_list[now]:
            if not visited[n]:
                dists[n] = min(dists[n], w)

    total = sum(dists)
    print(f'#{tc} {total}')