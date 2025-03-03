import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc, N = map(int, input().split())
    edges = list(map(int, input().split()))

    # 인접 리스트 만들기
    adj_list = [[] for _ in range(100)]

    for i in range(0, len(edges), 2):
        v, w = edges[i], edges[i + 1]
        adj_list[v].append(w)

    # DFS 탐색을 위한 초기 설정
    stack = [0]  # DFS를 위한 스택, 시작점 0를 추가
    visited = [0] * 100 # 방문 여부 저장 (0: 미방문, 1: 방문)
    visited[0] = 1  # 시작점 0 방문 처리
    result = 0  # 결과값 (S에서 G까지 도달 가능 여부)

    while stack:
        now = stack[-1]  # 현재 위치 (스택의 최상단 요소)

        if now == 99:  # 목표 노드 99에 도착하면
            result = 1  # 경로가 존재하므로 result를 1로 변경
            break  # 탐색 종료

        for next in adj_list[now]:  # 현재 노드의 인접 노드 탐색
            if not visited[next]:  # 방문하지 않은 노드라면
                stack.append(next)  # 스택에 추가 (다음 방문할 노드)
                visited[next] = 1  # 방문 처리
                break  # 바로 다음 노드로 진행 (DFS 방식)
        else:
            stack.pop()  # 방문할 곳이 없으면 백트래킹 (되돌아가기)

    print(f'#{tc} {result}')