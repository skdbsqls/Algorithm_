import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    deltas = [
        [0, 1],
        [1, 0],
        [-1, 0],
        [0, -1],
    ]

    visited = [0] * (N * N + 1)  # 어떤 자리에서 상하좌우에 1큰 수의 존재 여부를 담을 리스트
    for i in range(N):
        for j in range(N):
            num = matrix[i][j]

            # 상하좌우에
            for delta in deltas:
                ni, nj = i + delta[0], j + delta[1]

                # 유효한 인덱스이면서
                if 0 <= ni < N and 0 <= nj < N:
                    # 1큰 값이 있으면
                    if matrix[ni][nj] - num == 1:
                        visited[num] = 1  # 1큰 수의 존재 여부 표시(1)
                        break

    # 연속한 1의 개수 중 최대값 찾기
    max_start = max_rooms = 0  # 처음 출발해야 하는 방 번호, 최대 몇개의 방을 이동할 수 있는가
    cnt = 0  # 연속된 1의 개수
    for i in range(len(visited)):
        if visited[i] == 1:
            cnt += 1
        else:
            if cnt + 1 > max_rooms:
                max_start = i - cnt
                max_rooms = cnt + 1
            cnt = 0

    print(f'#{tc} {max_start} {max_rooms}')
