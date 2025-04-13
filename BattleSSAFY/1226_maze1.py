import sys
sys.stdin = open('mazeinput.txt')

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    result = 0  # 결과

    deltas = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]  # 델타

    queue = [[1, 1]]  # 시작점
    maze[1][1]  # 시작점 방문 처리

    while queue:
        ti, tj = queue.pop(0)  # 현위치

        # 델타 탐색
        for delta in deltas:
            ni, nj = ti + delta[0], tj + delta[1]  # 다음 위치

            # 유효한 인덱스
            if 0 <= ni < 16 and 0 <= nj < 16:
                # 도착 지점이면 성공
                if maze[ni][nj] == 3:
                    result = 1
                    break
                # 길(0)이면
                if maze[ni][nj] == 0:
                    queue.append([ni, nj])  # 큐에 넣고
                    maze[ni][nj] = 1  # 방문 처리

    print(f'#{tc} {result}')