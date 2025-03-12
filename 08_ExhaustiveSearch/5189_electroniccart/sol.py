import sys
sys.stdin = open('sample_input.txt')


# 가능한 경로 모두 구하기
def find_path(N, cnt, used, path):
    global paths

    if cnt == N - 1:
        path.append(1)  # 마지막에는 1로 돌아와야 함
        paths.append(path)
        return

    for i in range(2, N + 1):
        if not used[i]:
            used[i] = True
            find_path(N, cnt + 1, used, path + [i])
            used[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    paths = []  # 가능한 경로 모음
    # 숫자 범위, 몇 개 고를 지, 사용 여부, 경로(모든 경로는 1부터 시작)
    find_path(N, 0, [False for _ in range(N + 1)], [1])

    min_sum = 1e9  # 최소값
    # 최소값 구하기
    for path in paths:
        sum = 0  # 경로에 따른 배터리 소모량
        for i in range(N):
            A = path[i]  # A에서
            B = path[i + 1]  # B로 갈 때
            sum += matrix[A - 1][B - 1]  # 필요한 배터리량

        if min_sum > sum:
            min_sum = sum

    print(f'#{tc} {min_sum}')