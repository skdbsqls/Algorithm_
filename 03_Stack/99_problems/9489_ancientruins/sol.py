import sys

sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 가장 긴 구조물의 길이
    for i in range(N):
        for j in range(M):

            # 구조물이 있는 곳이라면
            if arr[i][j] == 1:
                garo = 1  # 가로 구조물
                sero = 1  # 세로 구조물

                # 가로 구조물의 길이 구하기
                for k in range(j + 1, M):  # 구조물이 있는 곳부터 끝까지
                    if arr[i][k] == 1:  # 구조물이 있다면
                        garo += 1  # 길이 + 1
                    else:  # 구조물이 없다면
                        break

                # 세로 구조물의 길이 구하기
                for l in range(i + 1, N):
                    if arr[l][j] == 1:
                        sero += 1
                    else:
                        break

                # 가로가 세로보다 길거나 같고, 최댓값보다도 크다면,
                if garo >= sero and garo > result:
                    result = garo
                # 세로가 가로보다 길거나 같고, 최댓값보다도 크다면,
                if sero >= garo and sero > result:
                    result = sero

    print(f'#{tc} {result}')