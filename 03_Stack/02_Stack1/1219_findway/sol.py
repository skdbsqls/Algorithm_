import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0
    adj_list = [[] for _ in range(100)]  # 인접 리스트

    # 인접 리스트 채우기
    for i in range(0, len(arr), 2):
        v, w = arr[i], arr[i + 1]  # 출발, 도착

        adj_list[v].append(w)

    # DFS 탐색을 위한 초기 설정
    stack = []  # DFS를 위한 스택
    visited = [0] * 100  # 방문 여부 체크 (0: 미방문, 1: 방문)
    v = 0  # 출발점 (0번 노드)

    while True:
        if v == 99:
            result = 1  # 도착점에 도달하면 result = 1

        if visited[v] == 0:
            visited[v] = 1  # 방문 표시

        for w in adj_list[v]:  # 현재 노드 v의 인접 노드 w 탐색
            if visited[w] == 0:  # 방문하지 않은 노드가 있다면
                stack.append(v)  # 현재 노드를 스택에 저장 (되돌아올 곳)
                v = w  # 이동
                break  # 이동했으면 반복 종료 (DFS 방식)
        else:
            if stack:
                v = stack.pop()  # 스택에서 꺼내 되돌아감
            else:
                break  # 스택이 비었으면 탐색 종료

    print(f'#{tc} {result}')


