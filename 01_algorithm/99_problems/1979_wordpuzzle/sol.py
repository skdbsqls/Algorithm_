import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수

    # 가로 퍼즐에서 찾기
    for i in range(N):
        length = 0  # 가로 퍼즐 단어의 길
        for j in range(N):
            if puzzle[i][j] == 1:  # 만약 1이면, 길이 세주기
                length += 1
            if puzzle[i][j] == 0 or j == N - 1:  # 만약 0이거나, 마지막 칸인 경우
                if length == K:  # 길이가 K인지 확인
                    result += 1
                length = 0  # 다음 가로 퍼즐 단어의 길이를 세기 위해서 길이 초기화

    # 세로 퍼즐에서 찾기
    for i in range(N):
        length = 0  # 세로 퍼즐 단어의 길
        for j in range(N):
            if puzzle[j][i] == 1:  # 만약 1이면, 길이 세주기
                length += 1
            if puzzle[j][i] == 0 or j == N - 1:  # 만약 0이거나, 마지막 칸인 경우
                if length == K:  # 길이가 K인지 확인
                    result += 1
                length = 0  # 다음 세로 퍼즐 단어의 길이를 세기 위해서 길이 초기화

    print(f'#{tc} {result}')