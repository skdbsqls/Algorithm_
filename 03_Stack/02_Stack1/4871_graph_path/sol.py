import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]  # 인접 리스트

    # 인접 리스트 채우기
    for edge in edges:
        start, end = edge

        adj_list[start].append(end)

    stack = [S]  # 스택(시작점)
    visited = [0] * (V + 1)  # 방문 표시
    visited[S] = 1  # 시작점 방문 표시
    result = 0  # 결과

    while stack:
        now = stack[-1]  # 현재 위치

        # 목표 지점에 도착하면
        if now == G:
            result = 1  # 결과를 1로 바꾸고
            break  # break

        # 인접한 노드 탐색
        for next in adj_list[now]:
            if not visited[next]:
                stack.append(next)
                visited[next] = 1
                break
        else:
            stack.pop()

    print(f'#{tc} {result}')