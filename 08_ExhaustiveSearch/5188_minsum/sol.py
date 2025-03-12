import sys
sys.stdin = open('sample_input.txt')


def recur(N, cur, end, total):
    global min_total

    # 도착하면 멈춰라...
    if cur[0] == end[0] and cur[1] == end[1]:
        min_total = min(total, min_total)  # 최소값 갱신
        return

    if 0 <= cur[0] + 1 < N:
        recur(N, [cur[0] + 1, cur[1]], end, total + board[cur[0] + 1][cur[1]])
    if 0 <= cur[1] + 1 < N:
        recur(N, [cur[0], cur[1] + 1], end, total + board[cur[0]][cur[1] + 1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    cur = [0, 0]  # 현재 좌표(시작점)
    end = [N - 1, N - 1]  # 도착점
    min_total = 1e9  # 최소값
    recur(N, cur, end, board[cur[0]][cur[1]])

    print(f'#{tc} {min_total}')