# import sys
# sys.stdin = open('input.txt')


def backtracing(row, total):
    global max_v

    # 가지치기: 현재 확률이 mav_v보다 작다면 탐색 중단
    if total * 100 <= max_v:
        return

    # 일을 모두 분배했으면, 최대값 갱신
    if row == N:
        total *= 100
        max_v = max(max_v, total)
        return

    for col in range(N):
        # 이전 사람이 선택한 일은 다음 사람이 할 수 없음
        if visited[col]:
            continue

        # 성공할 확률인 0인 건 볼 필요 없음
        if not arr[row][col]:
            continue

        visited[col] = 1
        backtracing(row + 1, total * (arr[row][col] * 0.01))
        visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    max_v = 0  # 최댓값
    backtracing(0, 1)

    print(f'#{tc} {max_v:.6f}')
