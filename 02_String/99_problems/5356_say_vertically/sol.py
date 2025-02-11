import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(5)]

    # 가장 긴 행의 길이 구하기
    max_len = len(board[0])
    for i in range(5):
        if max_len < len(board[i]):
            max_len = len(board[i])

    # 가장 긴 행의 길이 * 5 만큼의 2차원 배열 생성하기
    arr = [[0] * max_len for _ in range(5)]

    # 2차원 배열에 알맞은 위치에 글자 넣어주기
    for i in range(5):
        for j in range(len(board[i])):
            arr[i][j] = board[i][j]

    # 0이 아닌 글자가 있다면, 열 우선 순회로 결과에 담아주기
    result = ''
    for j in range(max_len):
        for i in range(5):
            if arr[i][j] != 0:
                result += arr[i][j]

    print(f'#{tc} {result}')