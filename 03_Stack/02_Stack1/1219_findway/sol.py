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

    stack = []  # 스택
    visited = [0] * 100  # 방문 표시
    v = 0  # 출발점에서 시작

    while True:
        # 도착점에 도달했다면,
        if v == 99:
            result = 1

        # 방문 표시
        if visited[v] == 0:
            visited[v] = 1

        # 인접한 곳 중
        for w in adj_list[v]:
            # 방문 안 한 곳이 있다면,
            if visited[w] == 0:
                stack.append(v)  # 현재 위치를 스택에 담고,
                v = w  # 위치 이동
                break

        # 인접한 곳 중 방문 안 한 곳이 없는데,
        else:
            # 스택이 비어 있지 않다면,
            if stack:
                v = stack.pop()  # 돌아감
            # 출발점으로 돌아왔다면,
            if stack[-1] == 0:
                break

    print(f'#{tc} {result}')


