import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    result = ''

    for i in range(N):
        for j in range(N - M + 1):

            # 가로 회문
            flag = True
            for k in range(M // 2):
                if matrix[i][j + k] != matrix[i][j + M - 1 - k]:
                    flag = False
                    break
            if flag:
                for g in range(j, j + M):
                    result += matrix[i][g]

            # 세로 회문
            flag = True
            for k in range(M // 2):
                if matrix[j + k][i] != matrix[j + M - 1 - k][i]:
                    flag= False
                    break
            if flag:
                for g in range(j, j + M):
                    result += matrix[g][i]

    print(f'#{tc} {result}')
