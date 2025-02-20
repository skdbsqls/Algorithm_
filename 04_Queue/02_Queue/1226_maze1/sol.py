import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    success = 0  # 결과

    # 탐색하기
    deltas = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]

    my_queue = [[1, 1]]  # 시작점은 (1, 1)
    maze[1][1] = 1  # 시작점 방문 처리

    # 더이상 방문할 곳이 없을 때까지 반복
    while my_queue:
        ti, tj = my_queue.pop(0)  # 큐에서 꺼내기(현위치)

        # 델타 탐색하기
        for delta in deltas:
            ni, nj = ti + delta[0], tj + delta[1]  # 다음 위치

            # 다음 위치가 유효한 인덱스이면서
            if 0 <= ni < 16 and 0 <= nj < 16:

                # 끝점(3)이면
                if maze[ni][nj] == 3:
                    success = 1  # 성공
                    break

                # 길(0)이면
                if maze[ni][nj] == 0:
                    my_queue.append([ni, nj])  # 큐에 넣고
                    maze[ni][nj] = 1  # 방문 표시

    print(f'#{tc} {success}')