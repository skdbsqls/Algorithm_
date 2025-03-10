import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 전선의 개수
    poles = [list(map(int, input().split())) for _ in range(N)]  # 전선 정보
    cnt = 0  # 교차점의 개수

    # 전선의 개수 만큼 반복
    for i in range(N):
        cur_start, cur_end = poles[i]  # 현재 전선의 시작점, 끝점

        # 이전 전선의 개수 만큼 반복
        for j in range(i):
            prev_start, prev_end = poles[j]  # 이전 전선의 시작점, 끝점

            # 이전 전선의 시작점이 현재 전선의 시작점보다 높으면서, 도착점은 낮을 때
            if prev_start > cur_start and prev_end < cur_end:
                cnt += 1
            # 이전 전선의 시작점이 현재 전선의 시작점보다 낮으면서, 도착점은 높을 때
            if prev_start < cur_start and prev_end > cur_end:
                cnt += 1

    print(f'#{tc} {cnt}')