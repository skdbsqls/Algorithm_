import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 최대로 많이 죽일 수 있는 파리 수

    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            sum = 0  # 죽은 파리의 수

            # 파리채 영역만큼 파리 죽이기
            for k in range(i, i + M):
                for l in range(j, j + M):
                    sum += arr[k][l]

            # 최댓값 갱신하기
            if result < sum:
                result = sum

    print(f'#{tc} {result}')