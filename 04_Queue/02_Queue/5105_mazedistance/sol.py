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
                si, sj = i, j

    # 탐색하기
    deltas = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    my_queue = [[si, sj, 0]]  # 큐(Queue) 생성 (현재 위치 + 거리 정보 포함)
    maze[si][sj] = 1  # 방문한 위치는 1로 변경 (중복 방문 방지)
    distance = 0  # 최단 거리 저장 변수

    while my_queue:  # 큐가 빌 때까지 반복
        ti, tj, count = my_queue.pop(0)  # 현재 위치 꺼내기

        for delta in deltas:  # 네 방향 탐색
            ni, nj = ti + delta[0], tj + delta[1]  # 다음 이동할 위치 계산

            if 0 <= ni < N and 0 <= nj < N:  # 미로 범위 내인지 확인
                if maze[ni][nj] == 0:  # 이동 가능한 길이라면
                    my_queue.append([ni, nj, count + 1])  # 큐에 추가 (거리 1 증가)
                    maze[ni][nj] = 1  # 방문 처리하여 다시 방문하지 않도록 설정
                elif maze[ni][nj] == 3:  # 도착점(3)에 도착하면
                    distance = count  # 현재 이동 거리 저장
                    break  # 탐색 종료

        if distance:  # 도착하면 더 이상 탐색할 필요 없음
            break

    print(f'#{tc} {distance}')