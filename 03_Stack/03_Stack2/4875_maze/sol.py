import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j

    # 탐색하기
    deltas = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]
    my_stack = [[si, sj]]
    visited = [[0] * N for _ in range(N)]
    result = 0  # 결과

    # 방문할 곳이 더이상 없을 때까지 반복
    while my_stack:
        ti, tj = my_stack.pop()  # 현재 위치 스택에서 꺼내기

        # 끝점(3)이면
        if maze[ti][tj] == 3:
            result = 1  # 성공
            break

        # 델타 탐색
        for delta in deltas:
            ni, nj = ti + delta[0], tj + delta[1]  # 다음 위치

            # 다음 위치가 유효한 인덱스이면서
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    my_stack.append([ni, nj])  # 스택에 넣어주고
                    maze[ni][nj] = 1  # 방문 표시

    print(f'#{tc} {result}')