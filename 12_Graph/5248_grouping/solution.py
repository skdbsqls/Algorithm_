import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N명, M장의 신청서
    edges = list(map(int, input().split()))

    adj_list = [[] for _ in range(N + 1)]
    for i in range(M):
        adj_list[edges[i*2]].append(edges[i * 2 + 1])
        adj_list[edges[i * 2 + 1]].append(edges[i * 2])

    visited = [False for _ in range(N + 1)]
    groups = 0
    for start in range(1, N + 1):
        if visited[start]:
            continue

        visited[start] = True
        stack = [start]

        while stack:
            now = stack.pop()

            for adj in adj_list[now]:

                if visited[adj]:
                    continue

                visited[adj] = True
                stack.append(adj)

        groups += 1

    print(f'#{tc} {groups}')