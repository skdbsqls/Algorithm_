import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for teat_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    coloring_book = [[0] * 10 for _ in range(10)]  # 색칠한 도화지

    for coloring in arr:
        start_i, start_j = coloring[0], coloring[1]  # 시작 좌표
        end_i, end_j = coloring[2], coloring[3]  # 끝 좌표
        color = coloring[4]  # 칠할 색상
        # print(start_i, start_j, end_i, end_j, color)

        # 색칠하기
        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                coloring_book[i][j] += color

    # 보라색이 된 칸 수 구하기
    result = 0  # 보라색 칸 수
    for i in range(10):
        for j in range(10):
            if coloring_book[i][j] >= 3:  # 3이상이면 보라색
                result += 1

    print(f'#{teat_case} {result}')